import logging
from typing import Any

from grpc_interceptor import ServerInterceptor


class ServerLoggingInterceptor(ServerInterceptor):
    """Basic logging interceptor class."""

    def __init__(self, logger: logging.Logger) -> None:
        super().__init__()
        self.logger = logger
        

    def intercept(self, method, request, context, method_name):
        """
        Intercepts method invokation - used to add logging & tracing in a clean way.
        """
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
        self.logger.debug(f"Successfully processed data, result: {str(result)}")
