import service_a_pb2, service_a_pb2_grpc


class ServiceAServicer(service_a_pb2_grpc.ServiceAServicer):
    """Provides methods that implement functionality of ServiceA server."""

    def ParseAndPass(self, request, context):
        # context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        # context.set_details('Method not implemented!')
        # raise NotImplementedError('Method not implemented!')

        return service_a_pb2._empty_pb2.Empty()  # noqa