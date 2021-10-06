# pylint: disable=cyclic-import
from __future__ import annotations

from typing import Mapping
from typing import Optional
from typing import Type
from typing import Union

from .http_exception import HTTPException


class ServerException(HTTPException):
    pass


class InternalServerErrorException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Internal Server Error'
        super().__init__(status_code=500, detail=detail)


class NotImplementedException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Not Implemented'
        super().__init__(status_code=501, detail=detail)


class BadGatewayException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Bad Gateway'
        super().__init__(status_code=502, detail=detail)


class ServiceUnavailableException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Service Unavailable'
        super().__init__(status_code=503, detail=detail)


class GatewayTimeoutException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Gateway Timeout'
        super().__init__(status_code=504, detail=detail)


class HttpVersionNotSupportedException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Http Version Not Supported'
        super().__init__(status_code=505, detail=detail)


class VariantAlsoNegotiatesException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Variant Also Negotiates'
        super().__init__(status_code=506, detail=detail)


class InsufficientStorageException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Insufficient Storage'
        super().__init__(status_code=507, detail=detail)


class LoopDetectedException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Loop Detected'
        super().__init__(status_code=508, detail=detail)


class NotExtendedException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Not Extended'
        super().__init__(status_code=510, detail=detail)


class NetworkAuthenticationRequiredException(ServerException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Network Authentication Required'
        super().__init__(status_code=511, detail=detail)


TYPE_SERVER_EXCEPTIONS = Type[  # pylint: disable=invalid-name
    Union[
        InternalServerErrorException,
        NotImplementedException,
        BadGatewayException,
        ServiceUnavailableException,
        GatewayTimeoutException,
        HttpVersionNotSupportedException,
        VariantAlsoNegotiatesException,
        InsufficientStorageException,
        LoopDetectedException,
        NotExtendedException,
        NetworkAuthenticationRequiredException,
    ]
]

SERVER_EXCEPTIONS: Mapping[int, TYPE_SERVER_EXCEPTIONS] = {
    500: InternalServerErrorException,
    501: NotImplementedException,
    502: BadGatewayException,
    503: ServiceUnavailableException,
    504: GatewayTimeoutException,
    505: HttpVersionNotSupportedException,
    506: VariantAlsoNegotiatesException,
    507: InsufficientStorageException,
    508: LoopDetectedException,
    510: NotExtendedException,
    511: NetworkAuthenticationRequiredException,
}
