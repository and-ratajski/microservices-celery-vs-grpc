FROM python:3.10-bullseye AS base
RUN python -m pip install --upgrade pip
WORKDIR /app

COPY ServiceD/.docker/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ServiceD/app .
RUN mkdir /protobufs
COPY _protobufs /protobufs

# Generate pb2 code
RUN python -m grpc_tools.protoc -I /protobufs \
    --python_out=. \
    --grpc_python_out=. \
    --mypy_out=. \
    /protobufs/test_string.proto \
    /protobufs/service_d.proto 

ENTRYPOINT ["python", "/app/app.py"]
