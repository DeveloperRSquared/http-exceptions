import inspect
from typing import Mapping
from typing import Type
from typing import Union

from http_exceptions.client_exceptions import CLIENT_EXCEPTIONS
from http_exceptions.client_exceptions import ClientException
from http_exceptions.http_exception import HTTPException
from http_exceptions.server_exceptions import SERVER_EXCEPTIONS
from http_exceptions.server_exceptions import ServerException


class TestHttpException:
    client_error_status_codes = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 444, 451]
    server_error_status_codes = [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
    all_error_status_codes = client_error_status_codes + server_error_status_codes

    all_exceptions: Mapping[int, Type[Union[ClientException, ServerException]]] = {**CLIENT_EXCEPTIONS, **SERVER_EXCEPTIONS}

    # check all status codes are mapped
    def test_status_codes(self) -> None:
        assert set(self.all_exceptions.keys()) == set(self.all_error_status_codes)

    # check from_status_code returns the expected exception for all status codes
    def test_from_status(self) -> None:
        for status_code in self.all_error_status_codes:
            http_exception = HTTPException.from_status_code(status_code=status_code)
            assert inspect.isclass(http_exception) and http_exception == self.all_exceptions[status_code]

    # check that from_status_code raises a ValueError if passed an invalid status
    def test_invalid_status(self) -> None:  # pylint: disable=no-self-use
        invalid_status_code = 0
        http_exception = HTTPException.from_status_code(status_code=invalid_status_code)
        assert inspect.isclass(http_exception) and http_exception == HTTPException
