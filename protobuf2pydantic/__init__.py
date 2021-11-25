from os import linesep
from typing import *  # noqa
from enum import IntEnum  # noqa

from google.protobuf.reflection import GeneratedProtocolMessageType
from google.protobuf.struct_pb2 import Struct  # noqa
from google.protobuf.timestamp_pb2 import Timestamp  # noqa
from google.protobuf.duration_pb2 import Duration  # noqa
from pydantic import BaseModel, Field  # noqa

from protobuf2pydantic.biz import msg2pydantic


def message2pydantic(message: GeneratedProtocolMessageType) -> Type[BaseModel]:
    """ convert a protobuf message object to pydantic model object """
    descriptor = message.DESCRIPTOR
    model_string = msg2pydantic(0, descriptor)
    getter_key = "getter"
    getter_string = f"def {getter_key}(): return {descriptor.name}"
    compile_string = model_string + linesep + getter_string
    compile_code = compile(compile_string, "<string>", "exec")
    sub_namespace = {k: v for k, v in globals().items() if not k.startswith("__")}
    exec(compile_code, sub_namespace)
    return sub_namespace[getter_key]()


msg2py = message2pydantic
