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
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Bad Request'
        super().__init__(status_code=400, detail=detail)


class UnauthorizedException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Unauthorized'
        super().__init__(status_code=401, detail=detail)


class PaymentRequiredException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Payment Required'
        super().__init__(status_code=402, detail=detail)


class ForbiddenException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Forbidden'
        super().__init__(status_code=403, detail=detail)


class NotFoundException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Not Found'
        super().__init__(status_code=404, detail=detail)


class MethodNotAllowedException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Method Not Allowed'
        super().__init__(status_code=405, detail=detail)


class NotAcceptableException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Not Acceptable'
        super().__init__(status_code=406, detail=detail)


class ProxyAuthenticationRequiredException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Proxy Authentication Required'
        super().__init__(status_code=407, detail=detail)


class RequestTimeoutException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Request Timeout'
        super().__init__(status_code=408, detail=detail)


class ConflictException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Conflict'
        super().__init__(status_code=409, detail=detail)


class GoneException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Gone'
        super().__init__(status_code=410, detail=detail)


class LengthRequiredException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Length Required'
        super().__init__(status_code=411, detail=detail)


class PreconditionFailedException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Precondition Failed'
        super().__init__(status_code=412, detail=detail)


class PayloadTooLargeException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Payload Too Large'
        super().__init__(status_code=413, detail=detail)


class UriTooLongException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'URI Too Long'
        super().__init__(status_code=414, detail=detail)


class UnsupportedMediaTypeException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Unsupported Media Type'
        super().__init__(status_code=415, detail=detail)


class RangeNotSatisfiableException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Range Not Satisfiable'
        super().__init__(status_code=416, detail=detail)


class ExpectationFailedException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Expectation Failed'
        super().__init__(status_code=417, detail=detail)


class ImATeapotException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'This server is a teapot, not a coffee machine'
        super().__init__(status_code=418, detail=detail)


class MisdirectedRequestException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Misdirected Request'
        super().__init__(status_code=421, detail=detail)


class UnprocessableEntityException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Unprocessable Entity'
        super().__init__(status_code=422, detail=detail)


class LockedException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Locked'
        super().__init__(status_code=423, detail=detail)


class FailedDependencyException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Failed Dependency'
        super().__init__(status_code=424, detail=detail)


class UpgradeRequiredException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Upgrade Required'
        super().__init__(status_code=426, detail=detail)


class PreconditionRequiredException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Precondition Required'
        super().__init__(status_code=428, detail=detail)


class TooManyRequestsException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Too Many Requests'
        super().__init__(status_code=429, detail=detail)


class RequestHeaderFieldsTooLargeException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Request Header Fields Too Large'
        super().__init__(status_code=431, detail=detail)


class NoResponseException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'No response'
        super().__init__(status_code=444, detail=detail)


class UnavailableForLegalReasonsException(ClientException):
    def __init__(self, detail: Optional[str] = None) -> None:
        detail = detail if detail else 'Unavailable For Legal Reasons'
        super().__init__(status_code=451, detail=detail)


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
        UriTooLongException,
        UnsupportedMediaTypeException,
        RangeNotSatisfiableException,
        ExpectationFailedException,
        ImATeapotException,
        MisdirectedRequestException,
        UnprocessableEntityException,
        LockedException,
        FailedDependencyException,
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
    414: UriTooLongException,
    415: UnsupportedMediaTypeException,
    416: RangeNotSatisfiableException,
    417: ExpectationFailedException,
    418: ImATeapotException,
    421: MisdirectedRequestException,
    422: UnprocessableEntityException,
    423: LockedException,
    424: FailedDependencyException,
    426: UpgradeRequiredException,
    428: PreconditionRequiredException,
    429: TooManyRequestsException,
    431: RequestHeaderFieldsTooLargeException,
    444: NoResponseException,
    451: UnavailableForLegalReasonsException,
}
