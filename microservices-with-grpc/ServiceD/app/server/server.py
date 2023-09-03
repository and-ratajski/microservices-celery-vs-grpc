import os
import logging

import service_d_pb2
from .db_config import test_table, engine


EmptyResponse = service_d_pb2.google_dot_protobuf_dot_empty__pb2.Empty


class ServiceDServicer:
    """Provides methods that implement functionality of ServiceA server."""

    def __init__(self, logger: logging.Logger) -> None:
        super().__init__()
        self.db_engine = engine
        self.logger = logger
        self.app_name = os.getenv("APP_NAME")

    def ParseAndPass(self, request, context) -> EmptyResponse:  # noqa
        """ServiceD's main task - saves string into DB."""
        self.logger.debug(
            f"Called ParseAndPass of {self.__class__.__name__} for {request}"
        )

        with self.db_engine.begin() as conn:
            conn.execute(
                test_table.insert().values(
                    test_string=request.test_string,
                    service=self.app_name,
                    created=request.created.ToDatetime(),
                ),
            )

        return EmptyResponse()
