from os import linesep
from typing import List
from functools import partial

from google.protobuf.reflection import GeneratedProtocolMessageType
from google.protobuf.descriptor import Descriptor, FieldDescriptor, EnumDescriptor

message_metaclasses = [GeneratedProtocolMessageType]
try:
    from google._upb._message import MessageMeta

    message_metaclasses.append(MessageMeta)
except ImportError:
    pass

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


def m(field: FieldDescriptor) -> str:
    return type_mapping[field.type].__name__


def convert_field(level: int, field: FieldDescriptor) -> str:
    level += 1
    field_type = field.type
    field_label = field.label
    was_mapping = False
    extra = None

    if field_type == FieldDescriptor.TYPE_ENUM:
        enum_type: EnumDescriptor = field.enum_type
        type_statement = enum_type.name
        class_statement = f"{tab * level}class {enum_type.name}(IntEnum):"
        field_statements = map(
            lambda value: f"{tab * (level + 1)}{value.name} = {value.index}",
            enum_type.values,
        )
        extra = linesep.join([class_statement, *field_statements])
        factory = "int"

    elif field_type == FieldDescriptor.TYPE_MESSAGE:
        type_statement: str = field.message_type.name
        if type_statement.endswith("Entry"):
            key, value = field.message_type.fields  # type: FieldDescriptor
            if value.type != 11:
                type_statement = f"Dict[{m(key)}, {m(value)}]"
            else:
                was_mapping = True
                type_statement = f"Dict[{m(key)}, {value.message_type.name}]"
            factory = "dict"
        elif type_statement == "Struct":
            type_statement = "Dict[str, Any]"
            factory = "dict"
        else:
            extra = msg2pydantic(level, field.message_type)
            factory = type_statement
    else:
        type_statement = m(field)
        factory = type_statement

    if field_label == FieldDescriptor.LABEL_REPEATED and not was_mapping:
        type_statement = f"List[{type_statement}]"
        factory = "list"

    default_statement = f" = Field(default_factory={factory})"
    if field_label == FieldDescriptor.LABEL_REQUIRED:
        default_statement = ""

    field_statement = f"{tab * level}{field.name}: {type_statement}{default_statement}"
    if not extra:
        return field_statement
    return linesep + extra + one_line + field_statement


def msg2pydantic(level: int, msg: Descriptor) -> str:
    class_statement = f"{tab * level}class {msg.name}(BaseModel):"
    field_statements = map(partial(convert_field, level), msg.fields)
    return linesep.join([class_statement, *field_statements])


def get_config(level: int):
    level += 1
    class_statement = f"{tab * level}class Config:"
    attribute_statement = f"{tab * (level + 1)}arbitrary_types_allowed = True"
    return linesep + class_statement + linesep + attribute_statement


def pb2_to_pydantic(module) -> str:
    pydantic_models: List[str] = []
    for i in dir(module):
        obj = getattr(module, i)
        if not any(isinstance(obj, metacls) for metacls in message_metaclasses):
            continue
        model_string = msg2pydantic(0, obj.DESCRIPTOR)
        pydantic_models.append(model_string)

    header = """from typing import List, Dict, Any
from enum import IntEnum

from pydantic import BaseModel, Field


"""
    return header + two_lines.join(pydantic_models)
