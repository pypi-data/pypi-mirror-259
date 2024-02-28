import json
import types, typing, inspect

OPENAPI_TARGET = None

DEFAULT_PARAM_TYPE = str

type_dict = { str: "string", int: 'integer', float: 'number', bool: 'boolean' }

class ParameterPropertie:
    type:        str
    description: str
    enum:        list
    required:    bool

    def __init__(self, param):
        if isinstance(param, types.UnionType):
            union_args = typing.get_args(param)
            if len(union_args) > 1:
                param = union_args[0]
        try:
            val = param()
        except:
            return

        if isinstance(val, bool):
            self.type = 'boolean'
        elif isinstance(val, str):
            self.type = 'string'
        elif isinstance(val, int):
            self.type = 'integer'
        elif isinstance(val, float):
            self.type = 'number'
        else:
            return
        
        if hasattr(param, '__metadata__') and isinstance(param.__metadata__, tuple):
            for meta in param.__metadata__:
                if isinstance(meta, str):
                    self.description = meta
                elif isinstance(meta, list):
                    self.enum = meta
                elif isinstance(meta, bool):
                    self.required = meta


    def to_dict(self) -> dict:
        data = {'type': self.type}
        if hasattr(self, 'description') and isinstance(self.description, str):
            data['description'] = self.description
        if hasattr(self, 'enum') and isinstance(self.enum, list) and len(self.enum) > 0:
            data['enum'] = self.enum
        return data


class FunctionParameter:
    type:       str  # object
    properties: dict[str: ParameterPropertie] # key: str, value: ParameterPropertie
    required:   list[str]

    def __init__(self):
        self.type = 'object'
        self.properties = dict[str: ParameterPropertie]()

    def to_dict(self) -> dict:
        data = {}
        properties = dict[str: dict]()
        self.required = list[str]()
        data['type'] = 'object' # self.type
        if isinstance(self.properties, dict) and len(self.properties) > 0:
            for name, prop in self.properties.items():
                if isinstance(prop, ParameterPropertie):
                    properties[name] = prop.to_dict()
                    if hasattr(prop, 'required') and prop.required:
                        self.required.append(name)
        data['properties'] = properties
        if len(self.required) > 0:
            data['required'] = self.required
        return data


class FunctionDefinition:
    name:        str
    description: str
    parameters:  FunctionParameter

    def __init__(self, func):
        if not isinstance(func, types.FunctionType):
            return
        self.name = func.__name__
        if hasattr(func, '__openapi_desc__'):
            self.description = func.__openapi_desc__
        self._parse_parameters(func)

    def _parse_parameters(self, func):
        self.parameters = FunctionParameter()
        fullargspec = inspect.getfullargspec(func)
        args_map, args_list = fullargspec.annotations, fullargspec.args
        args_num = 0 if args_list is None else len(args_list)
        defaults_num = 0 if fullargspec.defaults is None else len(fullargspec.defaults)
        required_num = args_num - defaults_num
        for i, name in enumerate(args_list):
            param = DEFAULT_PARAM_TYPE if args_map.get(name) is None else args_map.get(name)
            prop = ParameterPropertie(param)
            if hasattr(prop, 'type'):
                self.parameters.properties[name] = prop
                if i < required_num:
                    self.parameters.properties[name].required = True


    def to_dict(self) -> dict:
        data = {}
        if hasattr(self, 'name') and isinstance(self.name, str):
            data['name'] = self.name
        if hasattr(self, 'description') and isinstance(self.description, str):
            data['description'] = self.description
        if hasattr(self, 'parameters') and isinstance(self.parameters, FunctionParameter):
            data['parameters'] = self.parameters.to_dict()
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


def openapi_function(desc: str=''):
    def add_function_desc(func):
        global OPENAPI_TARGET
        OPENAPI_TARGET = func
        func.__openapi_desc__ = desc
        return func
    return add_function_desc


def parse_function_openapi(func) -> FunctionDefinition:
    return FunctionDefinition(func)


def parse_openapi_target() -> FunctionDefinition:
    return parse_function_openapi(OPENAPI_TARGET)


def exec_openapi_target(args_json: str) -> str:
    args = json.loads(args_json)
    result = OPENAPI_TARGET(**args)
    output = {}
    if isinstance(result, str) or isinstance(result, int) or \
    isinstance(result, float) or isinstance(result, bool) or \
    isinstance(result, dict) or isinstance(result, list) or \
    isinstance(result, set) or isinstance(result, tuple):
        output = result
    elif hasattr(result, "__dict__"):
        output = result.__dict__
    return json.dumps(output)
