import logging
import os
from concurrent import futures

import grpc
import service_b_pb2_grpc
from client.service_c_client import ServiceCClient
from server.interceptors import ServerLoggingInterceptor
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

service_c_client = ServiceCClient(logger)
service_b_servicer = ServiceBServicer(service_c_client, logger)

def serve() -> None:
    """Prepare and start ServiceB server."""
    interceptors = [ServerLoggingInterceptor(logger)]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1), interceptors=interceptors)
    service_b_pb2_grpc.add_ServiceBServicer_to_server(service_b_servicer, server)
    server.add_insecure_port(f"[::]:{app_port}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    if service_c_client.has_connection():
        logger.info(f"Starting {app_name} (gRPC Server) on port {app_port}...")
        serve()
    else:
        logger.critical("Couldn't connect to followup service, aborting...")
