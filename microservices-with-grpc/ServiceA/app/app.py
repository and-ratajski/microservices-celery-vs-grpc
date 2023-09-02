import logging
import os
from concurrent import futures

import grpc
import service_a_pb2_grpc
from server.interceptors import CustomServerInterceptor
from server.server import ServiceAServicer, channel


app_name = os.getenv("APP_NAME")
app_port = os.getenv("APP_PORT")
log_level = os.getenv("LOG_LEVEL")
conn_timeout = int(os.getenv("GRPC_CONNECTION_TIMEOUT"))

logger = logging.getLogger(app_name)
logger.setLevel(logging.getLevelName(log_level))
handler = logging.StreamHandler()
handler.setLevel(logging.getLevelName(log_level))
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def is_followup_service_up(channel) -> bool:
    try:
        logger.info(f"Trying to connect to followup service on channel: {channel}")
        grpc.channel_ready_future(channel).result(timeout=conn_timeout)
        return True
    except grpc.FutureTimeoutError:
        logger.warning("Connection timeout!")
        return False


def serve() -> None:
    interceptors = [CustomServerInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1), interceptors=interceptors)
    service_a_pb2_grpc.add_ServiceAServicer_to_server(ServiceAServicer(), server)
    server.add_insecure_port(f"[::]:{app_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    if is_followup_service_up(channel):
        logger.info(f"Starting ServiceA (gRPC Server) on port {app_port}...")
        serve()
    else:
        logger.critical("Couldn't connect to followup service, aborting...")

