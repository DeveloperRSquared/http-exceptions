# pylint: disable=import-outside-toplevel
from __future__ import annotations

from typing import Mapping
from typing import Optional
from typing import Type
from typing import Union


class HTTPException(Exception):
    def __init__(self, status_code: Optional[int] = None, message: Optional[str] = None) -> None:
        super().__init__()
        self.status_code = status_code or 500
        self.message = message

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(status_code={self.status_code!r}, message={self.message!r})'

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def from_status_code(cls, status_code: int) -> Type[HTTPException]:
        from .client_exceptions import CLIENT_EXCEPTIONS
        from .client_exceptions import TYPE_CLIENT_EXCEPTIONS
        from .server_exceptions import SERVER_EXCEPTIONS
        from .server_exceptions import TYPE_SERVER_EXCEPTIONS

        http_exceptions: Mapping[int, Union[TYPE_SERVER_EXCEPTIONS, TYPE_CLIENT_EXCEPTIONS]] = {**SERVER_EXCEPTIONS, **CLIENT_EXCEPTIONS}
        return http_exceptions.get(status_code, cls)
