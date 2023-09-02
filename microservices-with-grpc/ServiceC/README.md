# Service C

## Generate pb2 code (python)

```shell
python -m grpc_tools.protoc -I ../_protobufs --python_out=./app --grpc_python_out=./app --mypy_out=./app  ../_protobufs/test_string.proto ../_protobufs/service_c.proto ../_protobufs/service_d.proto
```

## Run service

```shell
docker-compose up -d
```

## Call server (from app directory)

```python
import grpc

from service_c_pb2_grpc import ServiceCStub
from test_string_pb2 import TestString
from google.protobuf.timestamp_pb2 import Timestamp

channel = grpc.insecure_channel("localhost:50051")
client = ServiceCStub(channel)
req = TestString(test_string="dummy")
req.created.GetCurrentTime()
client.ParseAndPass(req)
```

# Useful commands

<details>
<summary>Isort</summary>

If you want to run isort from within this service run:

```shell
isort --skip-glob="*_pb2*.py" .
```

</details>
</br>
