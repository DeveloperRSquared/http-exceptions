import pytest

from http_exceptions.client_exceptions import CLIENT_EXCEPTIONS
from http_exceptions.http_exception import HTTPException
from http_exceptions.server_exceptions import SERVER_EXCEPTIONS


class TestHttpException:
    client_error_status_codes = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 444, 451]
    server_error_status_codes = [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
    all_error_status_codes = client_error_status_codes + server_error_status_codes

    # check all status codes are mapped
    def test_status_codes(self) -> None:
        error_status_codes = {*CLIENT_EXCEPTIONS.keys(), *SERVER_EXCEPTIONS.keys()}
        assert error_status_codes == set(self.all_error_status_codes)

    # check from_status returns the expected exception for all status codes
    def test_from_status(self) -> None:
        all_exceptions = {**CLIENT_EXCEPTIONS, **SERVER_EXCEPTIONS}
        for status_code in self.all_error_status_codes:
            http_exception = HTTPException.from_status(status_code=status_code)
            assert isinstance(http_exception, all_exceptions[status_code])

    # check that from_status raises a ValueError if passed an invalid status
    def test_invalid_status(self) -> None:  # pylint: disable=no-self-use
        invalid_status_code = 0
        with pytest.raises(ValueError):
            HTTPException.from_status(status_code=invalid_status_code)
