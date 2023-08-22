import grpc
import logging
from concurrent import futures

import service_a_pb2_grpc
from server.server import ServiceAServicer

logger = logging.getLogger("ServiceA")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_a_pb2_grpc.add_ServiceAServicer_to_server(ServiceAServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logger.info("Starting ServiceA (as gRPC Server)...")
    serve()
