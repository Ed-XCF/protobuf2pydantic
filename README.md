# protobuf2pydantic

![GitHub](https://img.shields.io/github/license/Ed-XCF/protobuf2pydantic)
[![Build Status](https://www.travis-ci.org/Ed-XCF/protobuf2pydantic.svg?branch=main)](https://www.travis-ci.org/Ed-XCF/protobuf2pydantic)
[![codecov](https://codecov.io/gh/Ed-XCF/protobuf2pydantic/branch/main/graph/badge.svg?token=4YYBSTLS5F)](https://codecov.io/gh/Ed-XCF/protobuf2pydantic)
![PyPI](https://img.shields.io/pypi/v/protobuf2pydantic)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Ed-XCF/protobuf2pydantic.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Ed-XCF/protobuf2pydantic/context:python)

### Generate a file which include pydantic models by using protobuf.pb2 file
## Installation
```shell
pip3 install protobuf2pydantic
```

## Getting Started
### in CLI
```shell
pb2py ../test_pb2.py > wow.py
```

### in Python
```python
from protobuf2pydantic import msg2py
from pydantic import validator

import transaction_pb2


class AmountResponse(msg2py(transaction_pb2.AmountResponse)):
    @validator("amount")
    def non_negative(cls, v):
        assert v >= 0
        return v
```

### * Required proto file syntax = "proto3";
