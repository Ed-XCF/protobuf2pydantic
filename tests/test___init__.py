from pydantic.main import ModelMetaclass  # noqa

from protobuf2pydantic import message2pydantic
from tests.test_pb2 import TestMessage


def test_message2pydantic():
    klass = message2pydantic(TestMessage)
    assert isinstance(klass, ModelMetaclass)
    assert klass.__name__ == TestMessage.__name__


test_msg2py = test_message2pydantic
