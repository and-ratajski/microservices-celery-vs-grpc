import logging
import os

import grpc
import service_a_pb2
import service_a_pb2_grpc
from service_b_pb2_grpc import ServiceBStub
from test_string_pb2 import TestString

app_name = os.getenv("APP_NAME")
next_func_host = os.getenv("GRPC_FOLLOWUP_FUNC_HOST")
next_func_port = os.getenv("GRPC_FOLLOWUP_FUNC_PORT")

logger = logging.getLogger(app_name)
channel = grpc.insecure_channel(f"{next_func_host}:{next_func_port}")
client = ServiceBStub(channel)


class ServiceAServicer(service_a_pb2_grpc.ServiceAServicer):
    """Provides methods that implement functionality of ServiceA server."""

    def ParseAndPass(self, request, context):  # noqa
        logger.debug(f"Called ParseAndPass of {app_name} for {request}")
        parsed_string = request.test_string.swapcase()

        req = TestString(test_string=parsed_string, created=request.created)
        res = client.ParseAndPass(req)
        logger.debug(f"Returned response from ServiceB {res}")

        return service_a_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
