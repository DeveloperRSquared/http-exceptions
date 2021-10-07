# pylint: disable=import-outside-toplevel
from __future__ import annotations

from typing import Mapping
from typing import Union

from fastapi import HTTPException as FastAPIHTTPException


class HTTPException(FastAPIHTTPException):
    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def from_status_code(status_code: int) -> HTTPException:
        from .client_exceptions import CLIENT_EXCEPTIONS
        from .client_exceptions import TYPE_CLIENT_EXCEPTIONS
        from .server_exceptions import SERVER_EXCEPTIONS
        from .server_exceptions import TYPE_SERVER_EXCEPTIONS

        http_exceptions: Mapping[int, Union[TYPE_SERVER_EXCEPTIONS, TYPE_CLIENT_EXCEPTIONS]] = {**SERVER_EXCEPTIONS, **CLIENT_EXCEPTIONS}
        if status_code not in http_exceptions:
            raise ValueError(f"{status_code} is not a valid HTTP error code.")
        return http_exceptions[status_code]()
