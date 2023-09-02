import logging

import service_b_pb2
import service_b_pb2_grpc
from service_c_pb2_grpc import ServiceCStub

EmptyResponse = service_b_pb2.google_dot_protobuf_dot_empty__pb2.Empty


class ServiceBServicer(service_b_pb2_grpc.ServiceBServicer):
    """Provides methods that implement functionality of ServiceA server."""

    def __init__(self, service_c_client: ServiceCStub, logger: logging.Logger) -> None:
        super().__init__()
        self.service_c_client = service_c_client
        self.logger = logger
        
    def ParseAndPass(self, request, context) -> EmptyResponse:  # noqa
        """ServiceB's main task - parses dummy string to make it even dummier."""
        self.logger.debug(f"Called ParseAndPass of {self.__class__.__name__} for {request}")
        parsed_string = request.test_string.swapcase()

        request.test_string=parsed_string
        req = request
        res = self.service_c_client.invoke().ParseAndPass(req)

        self.logger.debug(f"Returned response from ServiceC: {res}")
        return EmptyResponse()
