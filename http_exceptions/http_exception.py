# pylint: disable=import-outside-toplevel
from __future__ import annotations

from functools import partial
from typing import Mapping
from typing import Optional
from typing import Type
from typing import Union


class HTTPException(Exception):
    def __init__(self, status_code: Optional[int] = None, message: Optional[str] = None) -> None:
        super().__init__()
        self.status_code = status_code if status_code is not None else 500
        self.message = message

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(status_code={self.status_code!r}, message={self.message!r})'

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.status_code == other.status_code and self.message == other.message

    def __hash__(self) -> int:
        return hash((self.status_code, self.message))

    @classmethod
    def from_status_code(cls, status_code: int) -> Union[Type[HTTPException], partial[HTTPException]]:
        from .client_exceptions import CLIENT_EXCEPTIONS
        from .client_exceptions import TYPE_CLIENT_EXCEPTIONS
        from .client_exceptions import ClientException
        from .server_exceptions import SERVER_EXCEPTIONS
        from .server_exceptions import TYPE_SERVER_EXCEPTIONS
        from .server_exceptions import ServerException

        http_exceptions: Mapping[int, Union[TYPE_SERVER_EXCEPTIONS, TYPE_CLIENT_EXCEPTIONS]] = {**SERVER_EXCEPTIONS, **CLIENT_EXCEPTIONS}
        exception_cls: Union[Type[HTTPException], partial[HTTPException]]
        if http_exceptions.get(status_code) is not None:
            exception_cls = http_exceptions[status_code]
        else:
            exception_base_cls: Union[Type[HTTPException], partial[HTTPException]]
            if 400 <= status_code < 500:
                exception_base_cls = ClientException
            elif 500 <= status_code < 600:
                exception_base_cls = ServerException
            else:
                exception_base_cls = HTTPException
            exception_cls = partial(exception_base_cls, status_code=status_code)
        return exception_cls
