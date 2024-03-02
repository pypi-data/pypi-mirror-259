
import * as flatbuffers from './flatbuffers.js';
import * as flexbuffers from './flexbuffers.js';
import * as zip from './zip.js';

const tflite = {};

tflite.ModelFactory = class {

    match(context) {
        const reader = context.peek('flatbuffers.binary');
        if (reader && reader.identifier === 'TFL3') {
            context.type = 'tflite.flatbuffers';
            context.target = reader;
            return;
        }
        const identifier = context.identifier;
        const extension = identifier.split('.').pop().toLowerCase();
        if (extension === 'tflite' && reader && reader.identifier) {
            const version = reader.uint32_(reader.root, 4, 0);
            if (version === 3) {
                context.type = 'tflite.flatbuffers';
                context.target = reader;
                return;
            }
        }
        const obj = context.peek('json');
        if (obj && obj.subgraphs && obj.operator_codes) {
            context.type = 'tflite.flatbuffers.json';
            context.target = obj;
            return;
        }
    }

    async open(context) {
        tflite.schema = await context.require('./tflite-schema');
        tflite.schema = tflite.schema.tflite;
        let model = null;
        const attachments = new Map();
        switch (context.type) {
            case 'tflite.flatbuffers.json': {
                try {
                    const reader = context.read('flatbuffers.text');
                    model = tflite.schema.Model.createText(reader);
                } catch (error) {
                    const message = error && error.message ? error.message : error.toString();
                    throw new tflite.Error(`File text format is not tflite.Model (${message.replace(/\.$/, '')}).`);
                }
                break;
            }
            case 'tflite.flatbuffers': {
                try {
                    const reader = context.target;
                    model = tflite.schema.Model.create(reader);
                } catch (error) {
                    const message = error && error.message ? error.message : error.toString();
                    throw new tflite.Error(`File format is not tflite.Model (${message.replace(/\.$/, '')}).`);
                }
                try {
                    const stream = context.stream;
                    const archive = zip.Archive.open(stream);
                    if (archive) {
                        for (const [name, value] of archive.entries) {
                            attachments.set(name, value);
                        }
                    }
                } catch (error) {
                    // continue regardless of error
                }
                break;
            }
            default: {
                throw new tflite.Error(`Unsupported TensorFlow Lite format '${context.type}'.`);
            }
        }
        const metadata = await context.metadata('tflite-metadata.json');
        return new tflite.Model(metadata, model);
    }
};

tflite.Model = class {

    constructor(metadata, model) {
        this._graphs = [];
        this._format = 'TensorFlow Lite';
        this._format = `${this._format} v${model.version}`;
        this._description = model.description || '';
        this._metadata = [];
        const builtinOperators = new Map();
        const upperCase = new Set(['2D', 'LSH', 'SVDF', 'RNN', 'L2', 'LSTM']);
        for (const key of Object.keys(tflite.schema.BuiltinOperator)) {
            const value = key === 'BATCH_MATMUL' ? 'BATCH_MAT_MUL' : key;
            const name = value.split('_').map((s) => (s.length < 1 || upperCase.has(s)) ? s : s[0] + s.substring(1).toLowerCase()).join('');
            const index = tflite.schema.BuiltinOperator[key];
            builtinOperators.set(index, name);
        }
        const operators = model.operator_codes.map((operator) => {
            const code = Math.max(operator.deprecated_builtin_code, operator.builtin_code || 0);
            const value = {};
            if (code === tflite.schema.BuiltinOperator.CUSTOM) {
                value.name = operator.custom_code ? operator.custom_code : 'Custom';
                value.version = operator.version;
                value.custom = true;
            } else {
                value.name = builtinOperators.has(code) ? builtinOperators.get(code) : code.toString();
                value.version = operator.version;
                value.custom = false;
            }
            return value;
        });
        let modelMetadata = null;
        for (const metadata of model.metadata) {
            const buffer = model.buffers[metadata.buffer];
            if (buffer) {
                switch (metadata.name) {
                    case 'min_runtime_version': {
                        const data = buffer.data || new Uint8Array(0);
                        this._runtime = new TextDecoder().decode(data);
                        break;
                    }
                    case 'TFLITE_METADATA': {
                        const data = buffer.data || new Uint8Array(0);
                        const reader = flatbuffers.BinaryReader.open(data);
                        if (tflite.schema.ModelMetadata.identifier(reader)) {
                            modelMetadata = tflite.schema.ModelMetadata.create(reader);
                            if (modelMetadata.name) {
                                this._name = modelMetadata.name;
                            }
                            if (modelMetadata.version) {
                                this._version = modelMetadata.version;
                            }
                            if (modelMetadata.description) {
                                this._description = this._description ? [this._description, modelMetadata.description].join(' ') : modelMetadata.description;
                            }
                            if (modelMetadata.author) {
                                this._metadata.push(new tflite.Argument('author', modelMetadata.author));
                            }
                            if (modelMetadata.license) {
                                this._metadata.push(new tflite.Argument('license', modelMetadata.license));
                            }
                        }
                        break;
                    }
                    default: {
                        break;
                    }
                }
            }
        }
        const subgraphs = model.subgraphs;
        const subgraphsMetadata = modelMetadata ? modelMetadata.subgraph_metadata : null;
        for (let i = 0; i < subgraphs.length; i++) {
            const subgraph = subgraphs[i];
            const name = subgraphs.length > 1 ? i.toString() : '';
            const subgraphMetadata = subgraphsMetadata && i < subgraphsMetadata.length ? subgraphsMetadata[i] : null;
            const graph = new tflite.Graph(metadata, subgraph, subgraphMetadata, name, operators, model);
            this._graphs.push(graph);
        }
    }

    get format() {
        return this._format;
    }

    get runtime() {
        return this._runtime;
    }

    get name() {
        return this._name;
    }

    get version() {
        return this._version;
    }

    get description() {
        return this._description;
    }

    get metadata() {
        return this._metadata;
    }

    get graphs() {
        return this._graphs;
    }
};

tflite.Graph = class {

    constructor(metadata, subgraph, subgraphMetadata, name, operators, model) {
        this._nodes = [];
        this._inputs = [];
        this._outputs = [];
        this._name = subgraph.name || name;
        const tensors = new Map();
        tensors.map = (index, metadata) => {
            if (index === -1) {
                return null;
            }
            if (!tensors.has(index)) {
                let tensor = { name: '' };
                let initializer = null;
                let description = '';
                let denotation = '';
                if (index < subgraph.tensors.length) {
                    tensor = subgraph.tensors[index];
                    const buffer = model.buffers[tensor.buffer];
                    const is_variable = tensor.is_variable;
                    const data = buffer ? buffer.data : null;
                    initializer = (data && data.length > 0) || is_variable ? new tflite.Tensor(index, tensor, buffer, is_variable) : null;
                }
                if (metadata) {
                    description = metadata.description;
                    const content = metadata.content;
                    if (content) {
                        const contentProperties = content.content_properties;
                        if (contentProperties instanceof tflite.schema.FeatureProperties) {
                            denotation = 'Feature';
                        } else if (contentProperties instanceof tflite.schema.ImageProperties) {
                            denotation = 'Image';
                            switch (contentProperties.color_space) {
                                case 0: denotation += '(Unknown)'; break;
                                case 1: denotation += '(RGB)'; break;
                                case 2: denotation += '(Grayscale)'; break;
                                default: throw tflite.Error(`Unsupported image color space '${contentProperties.color_space}'.`);
                            }
                        } else if (contentProperties instanceof tflite.schema.BoundingBoxProperties) {
                            denotation = 'BoundingBox';
                        } else if (contentProperties instanceof tflite.schema.AudioProperties) {
                            denotation = `Audio(${contentProperties.sample_rate},${contentProperties.channels})`;
                        }
                    }
                }
                const value = new tflite.Value(index, tensor, initializer, description, denotation);
                tensors.set(index, value);
            }
            return tensors.get(index);
        };
        const inputs = subgraph.inputs;
        for (let i = 0; i < inputs.length; i++) {
            const input = inputs[i];
            const metadata = subgraphMetadata && i < subgraphMetadata.input_tensor_metadata.length ? subgraphMetadata.input_tensor_metadata[i] : null;
            const value = tensors.map(input, metadata);
            const values = value ? [value] : [];
            const name = value ? value.name : '?';
            const argument = new tflite.Argument(name, values);
            this._inputs.push(argument);
        }
        const outputs = subgraph.outputs;
        for (let i = 0; i < outputs.length; i++) {
            const output = outputs[i];
            const metadata = subgraphMetadata && i < subgraphMetadata.output_tensor_metadata.length ? subgraphMetadata.output_tensor_metadata[i] : null;
            const value = tensors.map(output, metadata);
            const values = value ? [value] : [];
            const name = value ? value.name : '?';
            const argument = new tflite.Argument(name, values);
            this._outputs.push(argument);
        }
        for (let i = 0; i < subgraph.operators.length; i++) {
            const operator = subgraph.operators[i];
            const index = operator.opcode_index;
            const opcode = index < operators.length ? operators[index] : { name: `(${index})` };
            const node = new tflite.Node(metadata, operator, opcode, i.toString(), tensors);
            this._nodes.push(node);
        }
    }

    get name() {
        return this._name;
    }

    get inputs() {
        return this._inputs;
    }

    get outputs() {
        return this._outputs;
    }

    get nodes() {
        return this._nodes;
    }
};

tflite.Node = class {

    constructor(metadata, node, type, location, tensors) {
        this._location = location;
        this._type = type.custom ? { name: type.name, category: 'custom' } : metadata.type(type.name);
        this._inputs = [];
        this._outputs = [];
        this._attributes = [];
        if (node) {
            let inputs = [];
            let outputs = [];
            inputs = Array.from(node.inputs || new Int32Array(0));
            outputs = Array.from(node.outputs || new Int32Array(0));
            for (let i = 0; i < inputs.length;) {
                let count = 1;
                let name = null;
                let visible = true;
                const values = [];
                if (this._type && this._type.inputs && i < this._type.inputs.length) {
                    const input = this._type.inputs[i];
                    name = input.name;
                    if (input.list) {
                        count = inputs.length - i;
                    }
                    if (input.visible === false) {
                        visible = false;
                    }
                }
                const inputArray = inputs.slice(i, i + count);
                for (const index of inputArray) {
                    const value = tensors.map(index);
                    if (value) {
                        values.push(value);
                    }
                }
                i += count;
                name = name ? name : i.toString();
                const argument = new tflite.Argument(name, values, visible);
                this._inputs.push(argument);
            }
            for (let i = 0; i < outputs.length; i++) {
                const index = outputs[i];
                const value = tensors.map(index);
                const values = value ? [value] : [];
                let name = i.toString();
                if (this._type && this._type.outputs && i < this._type.outputs.length) {
                    const output = this._type.outputs[i];
                    if (output && output.name) {
                        name = output.name;
                    }
                }
                const argument = new tflite.Argument(name, values);
                this._outputs.push(argument);
            }
            if (type.custom && node.custom_options.length > 0) {
                let decoded = false;
                if (node.custom_options_format === tflite.schema.CustomOptionsFormat.FLEXBUFFERS) {
                    try {
                        const reader = flexbuffers.BinaryReader.open(node.custom_options);
                        if (reader) {
                            const custom_options = reader.read();
                            if (Array.isArray(custom_options)) {
                                const attribute = new tflite.Attribute(null, 'custom_options', custom_options);
                                this._attributes.push(attribute);
                                decoded = true;
                            } else if (custom_options) {
                                for (const [key, value] of Object.entries(custom_options)) {
                                    const schema = metadata.attribute(type.name, key);
                                    const attribute = new tflite.Attribute(schema, key, value);
                                    this._attributes.push(attribute);
                                }
                                decoded = true;
                            }
                        }
                    } catch (err) {
                        // continue regardless of error
                    }
                }
                if (!decoded) {
                    const schema = metadata.attribute(type.name, 'custom');
                    const attribute = new tflite.Attribute(schema, 'custom', Array.from(node.custom_options));
                    this._attributes.push(attribute);
                }
            }
            const options = node.builtin_options;
            if (options) {
                for (const [name, value] of Object.entries(options)) {
                    if (name === 'fused_activation_function' && value) {
                        if (value < 1 || value > 5) {
                            throw new tflite.Error(`Unsupported activation funtion index '${value}'.`);
                        }
                        const list = ['Unknown', 'Relu', 'ReluN1To1', 'Relu6', 'Tanh', 'SignBit'];
                        const type = list[value];
                        const node = new tflite.Node(metadata, null, { name: type }, null, []);
                        this._chain = [node];
                    }
                    const schema = metadata.attribute(type.name, name);
                    this._attributes.push(new tflite.Attribute(schema, name, value));
                }
            }
        }
    }

    get type() {
        return this._type;
    }

    get name() {
        return '';
    }

    get location() {
        return this._location;
    }

    get inputs() {
        return this._inputs;
    }

    get outputs() {
        return this._outputs;
    }

    get chain() {
        return this._chain;
    }

    get attributes() {
        return this._attributes;
    }
};

tflite.Attribute = class {

    constructor(metadata, name, value) {
        this._name = name;
        this._value = ArrayBuffer.isView(value) ? Array.from(value) : value;
        this._type = metadata && metadata.type ? metadata.type : null;
        if (this._name === 'fused_activation_function') {
            this._visible = false;
        }
        if (this._type) {
            this._value = tflite.Utility.enum(this._type, this._value);
        }
        if (metadata) {
            if (metadata.visible === false) {
                this._visible = false;
            } else if (metadata.default !== undefined) {
                value = this._value;
                if (typeof value === 'function') {
                    value = value();
                }
                if (value === metadata.default) {
                    this._visible = false;
                }
            }
        }
    }

    get name() {
        return this._name;
    }

    get type() {
        return this._type;
    }

    get value() {
        return this._value;
    }

    get visible() {
        return this._visible === false ? false : true;
    }
};

tflite.Argument = class {

    constructor(name, value, visible) {
        this._name = name;
        this._value = value;
        this._visible = visible === false ? false : true;
    }

    get name() {
        return this._name;
    }

    get visible() {
        return this._visible;
    }

    get value() {
        return this._value;
    }
};

tflite.Value = class {

    constructor(index, tensor, initializer, description, denotation) {
        const name = tensor.name || '';
        this.name = `${name}\n${index}`;
        this.location = index.toString();
        this.type = tensor.type !== undefined && tensor.shape !== undefined ? new tflite.TensorType(tensor, denotation) : null;
        this.initializer = initializer;
        this.description = description;
        const quantization = tensor.quantization;
        if (quantization && (quantization.scale.length > 0 || quantization.zero_point.length > 0 || quantization.min.length > 0 || quantization.max.length)) {
            this.quantization = {
                type: 'linear',
                dimension: quantization.quantized_dimension,
                scale: quantization.scale,
                offset: quantization.zero_point,
                min: quantization.min,
                max: quantization.max
            };
        }
    }
};

tflite.Tensor = class {

    constructor(index, tensor, buffer, is_variable) {
        this._location = index.toString();
        this._type = new tflite.TensorType(tensor);
        this._is_variable = is_variable;
        this._name = tensor.name;
        this._data = buffer.data.slice(0);
    }

    get category() {
        return this._is_variable ? 'Variable' : '';
    }

    get name() {
        return this._name;
    }

    get location() {
        return this._location;
    }

    get type() {
        return this._type;
    }

    get encoding() {
        switch (this._type.dataType) {
            case 'string': return '|';
            default: return '<';
        }
    }

    get values() {
        switch (this._type.dataType) {
            case 'string': {
                let offset = 0;
                const data = new DataView(this._data.buffer, this._data.byteOffset, this._data.byteLength);
                const count = data.getInt32(0, true);
                offset += 4;
                const offsetTable = [];
                for (let j = 0; j < count; j++) {
                    offsetTable.push(data.getInt32(offset, true));
                    offset += 4;
                }
                offsetTable.push(this._data.length);
                const stringTable = [];
                const utf8Decoder = new TextDecoder('utf-8');
                for (let k = 0; k < count; k++) {
                    const textArray = this._data.subarray(offsetTable[k], offsetTable[k + 1]);
                    stringTable.push(utf8Decoder.decode(textArray));
                }
                return stringTable;
            }
            default: {
                return this._data;
            }
        }
    }
};

tflite.TensorType = class {

    constructor(tensor, denotation) {
        this.dataType = tflite.Utility.dataType(tensor.type);
        this.shape = new tflite.TensorShape(Array.from(tensor.shape || []));
        this.denotation = denotation;
    }

    toString() {
        return this.dataType + this.shape.toString();
    }
};

tflite.TensorShape = class {

    constructor(dimensions) {
        this.dimensions = dimensions;
    }

    toString() {
        if (!this.dimensions || this.dimensions.length === 0) {
            return '';
        }
        return `[${this.dimensions.map((dimension) => dimension.toString()).join(',')}]`;
    }
};

tflite.Utility = class {

    static dataType(type) {
        if (!tflite.Utility._tensorTypeMap) {
            tflite.Utility._tensorTypeMap = new Map(Object.entries(tflite.schema.TensorType).map(([key, value]) => [value, key.toLowerCase()]));
            tflite.Utility._tensorTypeMap.set(6, 'boolean');
        }
        return tflite.Utility._tensorTypeMap.has(type) ? tflite.Utility._tensorTypeMap.get(type) : '?';
    }

    static enum(name, value) {
        const type = name && tflite.schema ? tflite.schema[name] : undefined;
        if (type) {
            tflite.Utility._enums = tflite.Utility._enums || new Map();
            if (!tflite.Utility._enums.has(name)) {
                const entries = new Map(Object.entries(type).map(([key, value]) => [value, key]));
                tflite.Utility._enums.set(name, entries);
            }
            const map = tflite.Utility._enums.get(name);
            if (map.has(value)) {
                return map.get(value);
            }
        }
        return value;
    }
};

tflite.Error = class extends Error {

    constructor(message) {
        super(message);
        this.name = 'Error loading TensorFlow Lite model.';
    }
};

export const ModelFactory = tflite.ModelFactory;
