# pylint: disable=cyclic-import
from __future__ import annotations

from typing import Mapping
from typing import Optional
from typing import Type
from typing import Union

from .http_exception import HTTPException


class ClientException(HTTPException):
    pass


class BadRequestException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Bad Request'
        super().__init__(status_code=400, message=message)


class UnauthorizedException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Unauthorized'
        super().__init__(status_code=401, message=message)


class PaymentRequiredException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Payment Required'
        super().__init__(status_code=402, message=message)


class ForbiddenException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Forbidden'
        super().__init__(status_code=403, message=message)


class NotFoundException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Not Found'
        super().__init__(status_code=404, message=message)


class MethodNotAllowedException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Method Not Allowed'
        super().__init__(status_code=405, message=message)


class NotAcceptableException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Not Acceptable'
        super().__init__(status_code=406, message=message)


class ProxyAuthenticationRequiredException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Proxy Authentication Required'
        super().__init__(status_code=407, message=message)


class RequestTimeoutException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Request Timeout'
        super().__init__(status_code=408, message=message)


class ConflictException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Conflict'
        super().__init__(status_code=409, message=message)


class GoneException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Gone'
        super().__init__(status_code=410, message=message)


class LengthRequiredException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Length Required'
        super().__init__(status_code=411, message=message)


class PreconditionFailedException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Precondition Failed'
        super().__init__(status_code=412, message=message)


class PayloadTooLargeException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Payload Too Large'
        super().__init__(status_code=413, message=message)


class URITooLongException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'URI Too Long'
        super().__init__(status_code=414, message=message)


class UnsupportedMediaTypeException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Unsupported Media Type'
        super().__init__(status_code=415, message=message)


class RangeNotSatisfiableException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Range Not Satisfiable'
        super().__init__(status_code=416, message=message)


class ExpectationFailedException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Expectation Failed'
        super().__init__(status_code=417, message=message)


class ImATeapotException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else "I'm a teapot"
        super().__init__(status_code=418, message=message)


class MisdirectedRequestException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Misdirected Request'
        super().__init__(status_code=421, message=message)


class UnprocessableEntityException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Unprocessable Entity'
        super().__init__(status_code=422, message=message)


class LockedException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Locked'
        super().__init__(status_code=423, message=message)


class FailedDependencyException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Failed Dependency'
        super().__init__(status_code=424, message=message)


class TooEarlyException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Too Early'
        super().__init__(status_code=425, message=message)


class UpgradeRequiredException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Upgrade Required'
        super().__init__(status_code=426, message=message)


class PreconditionRequiredException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Precondition Required'
        super().__init__(status_code=428, message=message)


class TooManyRequestsException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Too Many Requests'
        super().__init__(status_code=429, message=message)


class RequestHeaderFieldsTooLargeException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Request Header Fields Too Large'
        super().__init__(status_code=431, message=message)


class NoResponseException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'No response'
        super().__init__(status_code=444, message=message)


class UnavailableForLegalReasonsException(ClientException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message if message else 'Unavailable For Legal Reasons'
        super().__init__(status_code=451, message=message)


TYPE_CLIENT_EXCEPTIONS = Type[  # pylint: disable=invalid-name
    Union[
        BadRequestException,
        UnauthorizedException,
        PaymentRequiredException,
        ForbiddenException,
        NotFoundException,
        MethodNotAllowedException,
        NotAcceptableException,
        ProxyAuthenticationRequiredException,
        RequestTimeoutException,
        ConflictException,
        GoneException,
        LengthRequiredException,
        PreconditionFailedException,
        PayloadTooLargeException,
        URITooLongException,
        UnsupportedMediaTypeException,
        RangeNotSatisfiableException,
        ExpectationFailedException,
        ImATeapotException,
        MisdirectedRequestException,
        UnprocessableEntityException,
        LockedException,
        FailedDependencyException,
        TooEarlyException,
        UpgradeRequiredException,
        PreconditionRequiredException,
        TooManyRequestsException,
        RequestHeaderFieldsTooLargeException,
        NoResponseException,
        UnavailableForLegalReasonsException,
    ]
]

CLIENT_EXCEPTIONS: Mapping[int, TYPE_CLIENT_EXCEPTIONS] = {
    400: BadRequestException,
    401: UnauthorizedException,
    402: PaymentRequiredException,
    403: ForbiddenException,
    404: NotFoundException,
    405: MethodNotAllowedException,
    406: NotAcceptableException,
    407: ProxyAuthenticationRequiredException,
    408: RequestTimeoutException,
    409: ConflictException,
    410: GoneException,
    411: LengthRequiredException,
    412: PreconditionFailedException,
    413: PayloadTooLargeException,
    414: URITooLongException,
    415: UnsupportedMediaTypeException,
    416: RangeNotSatisfiableException,
    417: ExpectationFailedException,
    418: ImATeapotException,
    421: MisdirectedRequestException,
    422: UnprocessableEntityException,
    423: LockedException,
    424: FailedDependencyException,
    425: TooEarlyException,
    426: UpgradeRequiredException,
    428: PreconditionRequiredException,
    429: TooManyRequestsException,
    431: RequestHeaderFieldsTooLargeException,
    444: NoResponseException,
    451: UnavailableForLegalReasonsException,
}
