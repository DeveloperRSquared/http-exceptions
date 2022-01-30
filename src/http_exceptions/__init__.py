# isort: skip_file
# pylint: disable=wrong-import-position
try:
    from importlib.metadata import version
    from importlib.metadata import PackageNotFoundError
except ImportError:
    from importlib_metadata import version  # type: ignore[no-redef]
    from importlib_metadata import PackageNotFoundError  # type: ignore[no-redef]

try:
    __version__: str = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

from .http_exception import HTTPException

from .client_exceptions import ClientException
from .client_exceptions import BadRequestException
from .client_exceptions import UnauthorizedException
from .client_exceptions import PaymentRequiredException
from .client_exceptions import ForbiddenException
from .client_exceptions import NotFoundException
from .client_exceptions import MethodNotAllowedException
from .client_exceptions import NotAcceptableException
from .client_exceptions import ProxyAuthenticationRequiredException
from .client_exceptions import RequestTimeoutException
from .client_exceptions import ConflictException
from .client_exceptions import GoneException
from .client_exceptions import LengthRequiredException
from .client_exceptions import PreconditionFailedException
from .client_exceptions import PayloadTooLargeException
from .client_exceptions import URITooLongException
from .client_exceptions import UnsupportedMediaTypeException
from .client_exceptions import RangeNotSatisfiableException
from .client_exceptions import ExpectationFailedException
from .client_exceptions import ImATeapotException
from .client_exceptions import MisdirectedRequestException
from .client_exceptions import UnprocessableEntityException
from .client_exceptions import LockedException
from .client_exceptions import FailedDependencyException
from .client_exceptions import TooEarlyException
from .client_exceptions import UpgradeRequiredException
from .client_exceptions import PreconditionRequiredException
from .client_exceptions import TooManyRequestsException
from .client_exceptions import RequestHeaderFieldsTooLargeException
from .client_exceptions import NoResponseException
from .client_exceptions import UnavailableForLegalReasonsException

from .server_exceptions import ServerException
from .server_exceptions import InternalServerErrorException
from .server_exceptions import NotImplementedException
from .server_exceptions import BadGatewayException
from .server_exceptions import ServiceUnavailableException
from .server_exceptions import GatewayTimeoutException
from .server_exceptions import HTTPVersionNotSupportedException
from .server_exceptions import VariantAlsoNegotiatesException
from .server_exceptions import InsufficientStorageException
from .server_exceptions import LoopDetectedException
from .server_exceptions import NotExtendedException
from .server_exceptions import NetworkAuthenticationRequiredException
