import logging

import service_d_pb2

EmptyResponse = service_d_pb2.google_dot_protobuf_dot_empty__pb2.Empty


class ServiceDServicer():
    """Provides methods that implement functionality of ServiceA server."""

    def __init__(self, logger: logging.Logger) -> None:
        super().__init__()
        self.logger = logger
        
    def ParseAndPass(self, request, context) -> EmptyResponse:  # noqa
        """ServiceA's main task - parses dummy string to make it even dummier."""
        self.logger.debug(f"Called ParseAndPass of {self.__class__.__name__} for {request}")

        # TODO: db write

        return EmptyResponse()
