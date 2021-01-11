# protobuf2pydantic
### Generate a file which include pydantic models by using protobuf.pb2 file
## Installation

    $ pip install protobuf2pydantic

## Getting Started
### in CLI

    >>> pb2py ../test_pb2.py > wow.py

### in Python

    >>> from protobuf2pydantic import message2pydantic
    >>> from tests.test_pb2 import TestMessage
    >>>
    >>> klass = message2pydantic(TestMessage)
    >>> print(klass)
    <class 'TestMessage'>
    >>> print(type(klass))
    <class 'pydantic.main.ModelMetaclass'>

### * Required proto file syntax = "proto3";
### * No plan to support "oneof"
