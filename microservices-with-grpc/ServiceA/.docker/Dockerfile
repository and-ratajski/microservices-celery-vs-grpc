FROM python:3.10-bullseye AS base
RUN python -m pip install --upgrade pip
WORKDIR /app

COPY ServiceA/.docker/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ServiceA/app .
RUN mkdir /protobufs
COPY _protobufs /protobufs

RUN python -m grpc_tools.protoc -I /protobufs \
    --python_out=. \
    --grpc_python_out=. \
    --mypy_out=. \
    /protobufs/service_a.proto

ENTRYPOINT ["python", "/app/app.py"]
