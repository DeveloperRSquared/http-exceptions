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
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Internal Server Error'
        super().__init__(status_code=500, message=message)


class NotImplementedException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Not Implemented'
        super().__init__(status_code=501, message=message)


class BadGatewayException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Bad Gateway'
        super().__init__(status_code=502, message=message)


class ServiceUnavailableException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Service Unavailable'
        super().__init__(status_code=503, message=message)


class GatewayTimeoutException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Gateway Timeout'
        super().__init__(status_code=504, message=message)


class HTTPVersionNotSupportedException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'HTTP Version Not Supported'
        super().__init__(status_code=505, message=message)


class VariantAlsoNegotiatesException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Variant Also Negotiates'
        super().__init__(status_code=506, message=message)


class InsufficientStorageException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Insufficient Storage'
        super().__init__(status_code=507, message=message)


class LoopDetectedException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Loop Detected'
        super().__init__(status_code=508, message=message)


class NotExtendedException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Not Extended'
        super().__init__(status_code=510, message=message)


class NetworkAuthenticationRequiredException(ServerException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Network Authentication Required'
        super().__init__(status_code=511, message=message)


TYPE_SERVER_EXCEPTIONS = Type[  # pylint: disable=invalid-name
    Union[
        InternalServerErrorException,
        NotImplementedException,
        BadGatewayException,
        ServiceUnavailableException,
        GatewayTimeoutException,
        HTTPVersionNotSupportedException,
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
    505: HTTPVersionNotSupportedException,
    506: VariantAlsoNegotiatesException,
    507: InsufficientStorageException,
    508: LoopDetectedException,
    510: NotExtendedException,
    511: NetworkAuthenticationRequiredException,
}
