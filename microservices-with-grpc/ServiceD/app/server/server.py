import os
import logging

import service_d_pb2
from .db_config import db_session, TestTable

EmptyResponse = service_d_pb2.google_dot_protobuf_dot_empty__pb2.Empty


class ServiceDServicer():
    """Provides methods that implement functionality of ServiceA server."""

    def __init__(self, logger: logging.Logger) -> None:
        super().__init__()
        self.logger = logger
        self.app_name = os.getenv("APP_NAME")
        
    def ParseAndPass(self, request, context) -> EmptyResponse:  # noqa
        """ServiceA's main task - parses dummy string to make it even dummier."""
        self.logger.debug(
            f"Called ParseAndPass of {self.__class__.__name__} for {request}"
        )

        db_session.add(
            TestTable(
                test_string=request.test_string,
                service=self.app_name,
                created=request.created.ToDatetime()
            )
        )
        db_session.commit()
        db_session.remove()

        return EmptyResponse()
