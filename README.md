# http-exceptions

[![Build](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/build.yml/badge.svg)](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/build.yml)
[![Deploy](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/deploy.yml/badge.svg)](https://github.com/DeveloperRSquared/http-exceptions/actions/workflows/deploy.yml)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-brightgreen.svg)](#)
[![PyPI - License](https://img.shields.io/pypi/l/http-exceptions.svg)](https://pypi.org/project/http-exceptions/)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

Raisable HTTP Exceptions

## Available Exceptions

#### Client Exceptions

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
414: UriTooLongException
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

#### Server Exceptions

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
