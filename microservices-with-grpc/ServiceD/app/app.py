import logging
import os
from concurrent import futures

import grpc
import service_d_pb2_grpc
from server.interceptors import ServerLoggingInterceptor
from server.server import ServiceDServicer

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

service_d_servicer = ServiceDServicer(logger)

def serve() -> None:
    """Prepare and start ServiceD server."""
    interceptors = [ServerLoggingInterceptor(logger)]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1), interceptors=interceptors)
    service_d_pb2_grpc.add_ServiceDServicer_to_server(service_d_servicer, server)
    server.add_insecure_port(f"[::]:{app_port}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logger.info(f"Starting {app_name} (gRPC Server) on port {app_port}...")
    serve()
