import logging

import service_a_pb2
import service_a_pb2_grpc
from service_b_pb2_grpc import ServiceBStub

EmptyResponse = service_a_pb2.google_dot_protobuf_dot_empty__pb2.Empty


class ServiceAServicer(service_a_pb2_grpc.ServiceAServicer):
    """Provides methods that implement functionality of ServiceA server."""

    def __init__(self, service_b_client: ServiceBStub, logger: logging.Logger) -> None:
        super().__init__()
        self.service_b_client = service_b_client
        self.logger = logger
        
    def ParseAndPass(self, request, context) -> EmptyResponse:  # noqa
        """ServiceA's main task - parses dummy string to make it even dummier."""
        self.logger.debug(f"Called ParseAndPass of {self.__class__.__name__} for {request}")
        parsed_string = request.test_string.swapcase()

        request.test_string=parsed_string
        req = request
        res = self.service_b_client.invoke().ParseAndPass(req)

        self.logger.debug(f"Returned response from ServiceB: {res}")
        return EmptyResponse()
