from os import linesep
from typing import List, Dict
from functools import partial
from enum import IntEnum

from pydantic import BaseModel, Field
from google.protobuf.reflection import GeneratedProtocolMessageType
from google.protobuf.descriptor import Descriptor, FieldDescriptor, EnumDescriptor
from google.protobuf.struct_pb2 import Struct

tab = " " * 4
one_line, two_lines = linesep * 2, linesep * 3
type_mapping = {
    FieldDescriptor.TYPE_DOUBLE: float,
    FieldDescriptor.TYPE_FLOAT: float,
    FieldDescriptor.TYPE_INT64: int,
    FieldDescriptor.TYPE_UINT64: int,
    FieldDescriptor.TYPE_INT32: int,
    FieldDescriptor.TYPE_FIXED64: float,
    FieldDescriptor.TYPE_FIXED32: float,
    FieldDescriptor.TYPE_BOOL: bool,
    FieldDescriptor.TYPE_STRING: str,
    FieldDescriptor.TYPE_BYTES: str,
    FieldDescriptor.TYPE_UINT32: int,
    FieldDescriptor.TYPE_SFIXED32: float,
    FieldDescriptor.TYPE_SFIXED64: float,
    FieldDescriptor.TYPE_SINT32: int,
    FieldDescriptor.TYPE_SINT64: int,
}


def convert_field(level: int, field: FieldDescriptor) -> str:
    level += 1
    field_type = field.type
    extra = None

    if field_type == FieldDescriptor.TYPE_ENUM:
        enum_type: EnumDescriptor = field.enum_type
        type_statement = enum_type.name
        class_statement = f"{tab * level}class {enum_type.name}({IntEnum.__name__}):"
        field_statements = map(
            lambda value: f"{tab * (level + 1)}{value.name} = {value.index}",
            enum_type.values,
        )
        extra = linesep.join([class_statement, *field_statements])
        factory = int.__name__
    elif field_type == FieldDescriptor.TYPE_MESSAGE:
        type_statement = field.message_type.name
        if type_statement == Struct.__name__:
            type_statement = Dict._name  # noqa
            factory = dict.__name__
        else:
            extra = msg2pydantic(level, field.message_type)
            factory = type_statement
    else:
        type_statement = type_mapping[field_type].__name__
        factory = type_statement

    if field.label == FieldDescriptor.LABEL_REPEATED:
        type_statement = f"{List._name}[{type_statement}]"  # noqa
        factory = list.__name__

    default_statement = f"{Field.__name__}(default_factory={factory})"
    field_statement = f"{tab * level}{field.name}: {type_statement} = {default_statement}"
    if not extra:
        return field_statement
    return linesep + extra + one_line + field_statement


def msg2pydantic(level: int, msg: Descriptor) -> str:
    class_statement = f"{tab * level}class {msg.name}({BaseModel.__name__}):"
    field_statements = map(partial(convert_field, level), msg.fields)
    return linesep.join([class_statement, *field_statements])


def pb2_to_pydantic(module) -> str:
    pydantic_models: List[str] = []
    for i in dir(module):
        obj = getattr(module, i)
        if not isinstance(obj, GeneratedProtocolMessageType):
            continue
        model_string = msg2pydantic(0, obj.DESCRIPTOR)
        pydantic_models.append(model_string)

    header = """from typing import List, Dict
from enum import IntEnum

from pydantic import BaseModel, Field


"""
    return header + two_lines.join(pydantic_models)
