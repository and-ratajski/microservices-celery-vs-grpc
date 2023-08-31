# Service A

## Generate pb2 code (python)

```shell
python -m grpc_tools.protoc -I ../_protobufs --python_out=./app --grpc_python_out=./app --mypy_out=./app  ../_protobufs/test_string.proto ../_protobufs/service_b.proto ../_protobufs/service_c.proto
```

## Run service

```shell
docker-compose up -d
```

## Call server (from app directory)

```python
import grpc

from service_b_pb2_grpc import ServiceBStub
from test_string_pb2 import TestString

channel = grpc.insecure_channel("localhost:50051")
client = ServiceBStub(channel)
req = TestString(test_string="dummy")
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
