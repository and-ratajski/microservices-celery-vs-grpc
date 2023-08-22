# Service A

Generate python code

```shell
python -m grpc_tools.protoc -I ../_protobufs --python_out=./app --grpc_python_out=./app --mypy_out=./app ../_protobufs/service_a.proto
```