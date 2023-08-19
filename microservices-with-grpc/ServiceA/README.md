# Service A

Generate python code

```shell
python -m grpc_tools.protoc -I./protos --python_out=./app/pb2 --pyi_out=./app/pb2 --grpc_python_out=./app/pb2 ./protos/service_a.proto
```