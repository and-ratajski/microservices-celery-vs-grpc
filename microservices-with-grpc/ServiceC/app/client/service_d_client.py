import logging
import os
import sys

import grpc
from service_d_pb2_grpc import ServiceDStub


class ServiceDClient:
    """Singleton used to connect to and call ServiceB."""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(ServiceDClient, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger
        self.func_host = os.getenv("GRPC_FOLLOWUP_FUNC_HOST")
        self.func_port = os.getenv("GRPC_FOLLOWUP_FUNC_PORT")
        self.channel = grpc.insecure_channel(f"{self.func_host}:{self.func_port}")
        self.client = ServiceDStub(self.channel)

    def invoke(self) -> ServiceDStub:
        """Returns actual client instance."""
        return self.client

    def has_connection(self) -> bool:
        """Checks connection to the followup service."""
        try:
            conn_timeout = int(os.getenv("GRPC_CONNECTION_TIMEOUT"))
            self.logger.info(f"Checking connection with host: {self.func_host} on port: {self.func_port}...")
            grpc.channel_ready_future(self.channel).result(timeout=conn_timeout)
            return True
        except grpc.FutureTimeoutError:
            self.logger.warning("Connection timeout!")
            return False
        except ValueError:
            self.logger.critical("Connection timeout variable must be an unsigned int!")
            sys.exit(1)
