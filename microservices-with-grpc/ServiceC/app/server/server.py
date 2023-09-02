import logging

import service_c_pb2
import service_c_pb2_grpc
from service_d_pb2_grpc import ServiceDStub

EmptyResponse = service_c_pb2.google_dot_protobuf_dot_empty__pb2.Empty


class ServiceCServicer(service_c_pb2_grpc.ServiceCServicer):
    """Provides methods that implement functionality of ServiceA server."""

    def __init__(self, service_d_client: ServiceDStub, logger: logging.Logger) -> None:
        super().__init__()
        self.service_d_client = service_d_client
        self.logger = logger
        
    def ParseAndPass(self, request, context) -> EmptyResponse:  # noqa
        """ServiceC's main task - parses dummy string to make it even dummier."""
        self.logger.debug(f"Called ParseAndPass of {self.__class__.__name__} for {request}")
        parsed_string = request.test_string.swapcase()

        request.test_string=parsed_string
        req = request
        res = self.service_d_client.invoke().ParseAndPass(req)

        self.logger.debug(f"Returned response from ServiceD: {res}")
        return EmptyResponse()
