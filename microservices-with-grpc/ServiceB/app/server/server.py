import logging
import os

import grpc
import service_b_pb2
import service_b_pb2_grpc

# import service_c_pb2
# import service_c_pb2_grpc

app_name = os.getenv("APP_NAME")
next_func_host = os.getenv("GRPC_FOLLOWUP_FUNC_HOST")
next_func_port = os.getenv("APP_NAME")

logger = logging.getLogger(app_name)
channel = grpc.insecure_channel(f"{next_func_host}:{next_func_port}")
client = service_b_pb2_grpc.ServiceBStub(channel)


class ServiceBServicer(service_b_pb2_grpc.ServiceBServicer):
    """Provides methods that implement functionality of ServiceA server."""

    def ParseAndPass(self, request, context):  # noqa
        # context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        # context.set_details('Method not implemented!')
        # raise NotImplementedError('Method not implemented!')
        logger.debug(f"Called ParseAndPass of {app_name} for {request} and {context}")
        # parsed_string = request.test_string.swapcase()
        #
        # req = service_b_pb2.TestString(test_string=parsed_string)
        # res = client.ParseAndPass(req)

        return service_b_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
