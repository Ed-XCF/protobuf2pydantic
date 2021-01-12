# protobuf2pydantic

![GitHub](https://img.shields.io/github/license/Ed-XCF/protobuf2pydantic)
[![Build Status](https://www.travis-ci.org/Ed-XCF/protobuf2pydantic.svg?branch=main)](https://www.travis-ci.org/Ed-XCF/protobuf2pydantic)
[![codecov](https://codecov.io/gh/Ed-XCF/protobuf2pydantic/branch/main/graph/badge.svg?token=4YYBSTLS5F)](https://codecov.io/gh/Ed-XCF/protobuf2pydantic)
![PyPI](https://img.shields.io/pypi/v/protobuf2pydantic)

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
