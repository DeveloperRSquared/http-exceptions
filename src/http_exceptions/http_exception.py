# pylint: disable=import-outside-toplevel
from __future__ import annotations

from typing import Mapping
from typing import Type
from typing import Union

from fastapi import HTTPException as FastAPIHTTPException


class HTTPException(FastAPIHTTPException):
    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def from_status(status_code: int) -> HTTPException:
        from .client_exceptions import CLIENT_EXCEPTIONS
        from .client_exceptions import ClientException
        from .server_exceptions import SERVER_EXCEPTIONS
        from .server_exceptions import ServerException

        http_exceptions: Mapping[int, Type[Union[ClientException, ServerException]]] = {**SERVER_EXCEPTIONS, **CLIENT_EXCEPTIONS}
        if status_code not in http_exceptions:
            raise ValueError(f"{status_code} is not a valid HTTP error code.")
        return http_exceptions[status_code]()
