import logging
import os

import service_a_pb2
import service_a_pb2_grpc

app_name = os.getenv("APP_NAME")
logger = logging.getLogger(app_name)


class ServiceAServicer(service_a_pb2_grpc.ServiceAServicer):
    """Provides methods that implement functionality of ServiceA server."""

    def ParseAndPass(self, request, context):  # noqa
        # context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        # context.set_details('Method not implemented!')
        # raise NotImplementedError('Method not implemented!')
        logger.debug(f"Called ParseAndPass of {app_name} for {request} and {context}")

        return service_a_pb2.google_dot_protobuf_dot_empty__pb2.Empty()  # noqa