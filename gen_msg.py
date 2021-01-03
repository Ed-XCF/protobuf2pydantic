from os import linesep
from typing import List
from functools import partial
from dataclasses import dataclass, field

from google.protobuf.reflection import GeneratedProtocolMessageType
from google.protobuf.descriptor import Descriptor, FieldDescriptor, EnumDescriptor, EnumValueDescriptor
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
    FieldDescriptor.TYPE_ENUM: int,
    FieldDescriptor.TYPE_SFIXED32: float,
    FieldDescriptor.TYPE_SFIXED64: float,
    FieldDescriptor.TYPE_SINT32: int,
    FieldDescriptor.TYPE_SINT64: int,
}


@dataclass
class Field:
    level: int
    name: str
    descriptor: FieldDescriptor

    @property
    def sub_level(self):
        return self.level + 1

    @property
    def tab(self):
        return self.level * tab

    @property
    def tab_tab(self):
        return self.sub_level * tab

    @property
    def type_statement(self) -> str:
        if self.descriptor.label == FieldDescriptor.LABEL_REPEATED:
            return f"typing.List[{self.descriptor.name}]"
        else:
            return self.descriptor.name


@dataclass
class EnumField(Field):
    descriptor: EnumDescriptor

    @property
    def extra_class_statement(self):
        return f"{self.tab}class {self.descriptor.name}(enum.IntEnum):"

    def extra_class_field_statement(self, value: EnumValueDescriptor):
        return f"{self.tab_tab}{value.name} = {value.index}"

    @property
    def field_statement(self):
        return f"{self.tab}{self.name}: {self.type_statement}"

    @property
    def field(self):
        return linesep.join([
            self.extra_class_statement,
            *map(self.extra_class_field_statement, self.descriptor.values),
            linesep,
            self.field_statement,
        ])


def covert_enum(level: int, enum: EnumDescriptor) -> str:
    f = EnumField(level, "", enum)
    return linesep.join([
        f.extra_class_statement,
        *map(f.extra_class_field_statement, enum.values)
    ])


def convert_field(level: int, field: FieldDescriptor) -> str:
    field_type = field.type

    if field_type == FieldDescriptor.TYPE_ENUM:
        type_statement = "enum.IntEnum"
        extra = covert_enum(level + 1, field.enum_type)
    elif field_type != FieldDescriptor.TYPE_MESSAGE:
        type_statement = type_mapping[field_type].__name__
        extra = None
    else:
        type_statement = field.message_type.name
        if type_statement == Struct.__name__:
            type_statement = "typing.Dict"
        else:
            extra = msg2pydantic(level + 1, field.message_type)

    if field.label == FieldDescriptor.LABEL_REPEATED:
        type_statement = f"typing.List[{type_statement}]"

    field_statement = f"{tab * (level + 1)}{field.name}: {type_statement}"
    if not extra:
        return field_statement
    return linesep + extra + one_line + field_statement


def msg2pydantic(level: int, msg: Descriptor) -> str:
    class_statement = f"{tab * level}class {msg.name}(BaseModel):"
    field_statements = map(partial(convert_field, level), msg.fields)
    return linesep.join([class_statement, *field_statements])


def gen_pydantic(module) -> str:
    pydantic_models: List[str] = []
    for i in dir(module):
        obj = getattr(module, i)
        if not isinstance(obj, GeneratedProtocolMessageType):
            continue
        model_string = msg2pydantic(0, obj.DESCRIPTOR)
        pydantic_models.append(model_string)
    return two_lines.join(pydantic_models)


if __name__ == '__main__':
    # from test import celery_task_pb2 as pb2
    from test1 import test_pb2 as pb2
    print(gen_pydantic(pb2))
