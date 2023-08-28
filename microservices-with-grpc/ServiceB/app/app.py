import logging
import os
from concurrent import futures

import grpc
import service_b_pb2_grpc
from server.interceptors import CustomServerInterceptor
from server.server import ServiceBServicer

app_name = os.getenv("APP_NAME")
app_port = os.getenv("APP_PORT")
log_level = os.getenv("LOG_LEVEL")

logger = logging.getLogger(app_name)
logger.setLevel(logging.getLevelName(log_level))
handler = logging.StreamHandler()
handler.setLevel(logging.getLevelName(log_level))
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def serve():
    interceptors = [CustomServerInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1), interceptors=interceptors)
    service_b_pb2_grpc.add_ServiceBServicer_to_server(ServiceBServicer(), server)
    server.add_insecure_port(f"[::]:{app_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logger.info(f"Starting ServiceB (gRPC Server) on port {app_port}...")
    serve()
