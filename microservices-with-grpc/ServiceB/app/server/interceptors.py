import logging
import os
from typing import Any

from grpc_interceptor import ServerInterceptor


class CustomServerInterceptor(ServerInterceptor):

    def __init__(self, *args, **kwargs):
        app_name = os.getenv("APP_NAME")
        self.logger = logging.getLogger(app_name)
        super().__init__(*args, **kwargs)

    def intercept(self, method, request, context, method_name):
        try:
            result = method(request, context)
        except Exception as e:
            self.log_error(e)
            raise
        else:
            self.log_success(result)
            return result

    def log_error(self, e: Exception) -> None:
        self.logger.error(e)

    def log_success(self, result: Any) -> None:
        self.logger.info(f"Successfully processed data, result: {str(result)}")
