# Service A

Generate python code

```shell
python -m grpc_tools.protoc -I ../_protobufs --python_out=./app --grpc_python_out=./app --mypy_out=./app ../_protobufs/service_a.proto
```

Run service (server)

```shell
docker-compose up -d
```

Call server (from app directory)

```python
import grpc

from service_a_pb2_grpc import ServiceAStub
from service_a_pb2 import TestString

channel = grpc.insecure_channel("localhost:50051")
client = ServiceAStub(channel)
req = TestString(test_string="dummy")
client.ParseAndPass(req)
```

If you want to run isort from within this service run:

```shell
isort --skip-glob="*_pb2*.py" .
```
