# http-exceptions

[![Build](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/build.yml/badge.svg)](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/build.yml)
[![Deploy](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/deploy.yml/badge.svg)](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/deploy.yml)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-brightgreen.svg)](#)
[![PyPI - License](https://img.shields.io/pypi/l/http-exceptions.svg)](https://pypi.org/project/http-exceptions/)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

Raisable HTTP Exceptions

## What is it good for?

1. Save writing boilerplate code:

    ```py
    # e.g. app/internal.py
    def some_function() -> None:
        raise SomeError()

    # e.g. app/api.py
    def api(request: Request) -> Response:
    try:
        response = some_function()
    except SomeError:
        response = Response(status_code=403)
    return response
    ```

    into this:

    ```py
    # e.g. app/internal.py
    from http_exceptions import HTTPException

    def some_function():
        raise ForbiddenException()

    # e.g. app/api.py
    def api(request):
        return some_function()
    ```

2. Dynamic exception raising:

    ```py
    from http_exceptions import HTTPException

    def raise_from_status(response: Response) -> None
        if 400 <= response.status < 600:
            raise HTTPException.from_status_code(status_code=response.status)(message=response.text)

    >>> response = Response(status_code=403)
    >>> raise_from_status(response=response)  # ForbiddenException raised
    ```

## Install http-exceptions

Simply install the package from [PyPI](pypi.org/project/http-exceptions/).

```bash
pip install -U http-exceptions
```

And that is it, you are ready to raise HTTP Exceptions.

## What else?

### `HTTPException`

Base class that provides all the exceptions to be raised.

### `HTTPExceptions.from_status_code(status_code)`

Returns the relevant Exception corresponding to `status_code`

e.g. `HTTPExceptions.from_status_code(status_code=431)` -> `RequestHeaderFieldsTooLargeException`

### `ClientException`

Subclass of `HTTPException` serving as a base class for exceptions with statuses in the [400, 499] range.

```py
from http_exceptions import ClientException

try:
    raise RequestHeaderFieldsTooLargeException
except ClientException:
    # exception is caught here
    pass
```

### `ServerException`

Subclass of `HTTPException` serving as a base class for exceptions with statuses in the [500, 599] range.

```py
from http_exceptions import ServerException

try:
    raise HTTPVersionNotSupportedException
except ServerException:
    # exception is caught here
    pass
```

## Available Exceptions

### Client Exceptions: `400 <= status <= 499`

```py
400: BadRequestException
401: UnauthorizedException
402: PaymentRequiredException
403: ForbiddenException
404: NotFoundException
405: MethodNotAllowedException
406: NotAcceptableException
407: ProxyAuthenticationRequiredException
408: RequestTimeoutException
409: ConflictException
410: GoneException
411: LengthRequiredException
412: PreconditionFailedException
413: PayloadTooLargeException
414: URITooLongException
415: UnsupportedMediaTypeException
416: RangeNotSatisfiableException
417: ExpectationFailedException
418: ImATeapotException
421: MisdirectedRequestException
422: UnprocessableEntityException
423: LockedException
424: FailedDependencyException
425: TooEarlyException
426: UpgradeRequiredException
428: PreconditionRequiredException
429: TooManyRequestsException
431: RequestHeaderFieldsTooLargeException
444: NoResponseException
451: UnavailableForLegalReasonsException
```

### Server Exceptions: `500 <= status <= 599`

```py
500: InternalServerErrorException
501: NotImplementedException
502: BadGatewayException
503: ServiceUnavailableException
504: GatewayTimeoutException
505: HTTPVersionNotSupportedException
506: VariantAlsoNegotiatesException
507: InsufficientStorageException
508: LoopDetectedException
510: NotExtendedException
511: NetworkAuthenticationRequiredException
```

## License

This project is licensed under the terms of the [MIT license](./LICENSE).
