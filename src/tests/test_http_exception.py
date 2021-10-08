import inspect
from functools import partial
from typing import Mapping
from typing import Optional
from typing import Type
from typing import Union

from http_exceptions import HTTPException
from http_exceptions.client_exceptions import CLIENT_EXCEPTIONS
from http_exceptions.client_exceptions import ClientException
from http_exceptions.server_exceptions import SERVER_EXCEPTIONS
from http_exceptions.server_exceptions import ServerException


class SimilarHTTPException(Exception):
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


class HttpExceptionTestCase:
    client_error_status_codes = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 444, 451]
    server_error_status_codes = [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
    all_error_status_codes = client_error_status_codes + server_error_status_codes

    all_exception_classes: Mapping[int, Type[Union[ClientException, ServerException]]] = {**CLIENT_EXCEPTIONS, **SERVER_EXCEPTIONS}


class TestHTTPException(HttpExceptionTestCase):
    # check all status codes are mapped
    def test_status_codes(self) -> None:
        assert set(self.all_exception_classes.keys()) == set(self.all_error_status_codes)

    # check HTTPException is an instance of exception
    def test_instance_of_exception(self) -> None:  # pylint: disable=no-self-use
        http_exception = HTTPException()
        assert isinstance(http_exception, Exception)
        assert isinstance(http_exception, HTTPException)


class TestFromStatusCode(HttpExceptionTestCase):
    # check from_status_code returns the expected exception for all status codes
    def test_from_status_code(self) -> None:
        for status_code in self.all_error_status_codes:
            http_exception_cls = HTTPException.from_status_code(status_code=status_code)
            assert inspect.isclass(http_exception_cls)
            assert http_exception_cls == self.all_exception_classes[status_code]
            message = 'HTTP Exception'
            http_exception = http_exception_cls(message=message)
            assert isinstance(http_exception, HTTPException)
            assert http_exception.status_code == status_code
            assert http_exception.message == message

    # check that from_status_code returns a HTTPException when the status_code doesn't match one of the client/server exceptions
    def test_invalid_status(self) -> None:  # pylint: disable=no-self-use
        invalid_status_code = 0
        http_exception_cls = HTTPException.from_status_code(status_code=invalid_status_code)
        assert isinstance(http_exception_cls, partial)
        assert http_exception_cls.keywords['status_code'] == invalid_status_code
        message = 'HTTP Exception'
        http_exception = http_exception_cls(message=message)
        assert isinstance(http_exception, HTTPException)
        assert http_exception.status_code == invalid_status_code
        assert http_exception.message == message


class TestCatch(HttpExceptionTestCase):
    # check that all client and server exceptions are caught by HTTPException
    def test_catch_all_exceptions(self) -> None:
        for http_exception_cls in self.all_exception_classes.values():
            http_exception = http_exception_cls()
            try:
                raise http_exception
            except HTTPException:
                pass

    # check that ClientException and ServerException are caught by HTTPException
    def test_catch_client_and_server_exceptions(self) -> None:  # pylint: disable=no-self-use
        for http_exception_cls in [ClientException, ServerException]:
            http_exception = http_exception_cls()
            try:
                raise http_exception
            except HTTPException:
                pass


class TestEquality(HttpExceptionTestCase):
    # check two instances of HTTPException can be equal
    def test_equivalent_http_exceptions(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        message = 'HTTP Exception'
        http_exception_1 = HTTPException(status_code=status_code, message=message)
        http_exception_2 = HTTPException(status_code=status_code, message=message)
        assert http_exception_1 == http_exception_2

    # check instance of HTTPException not equal to a similar HTTPExcpetion with the same fields
    def test_not_equal_to_another_class(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        message = 'HTTP Exception'
        http_exception_1 = HTTPException(status_code=status_code, message=message)
        http_exception_2 = SimilarHTTPException(status_code=status_code, message=message)
        assert http_exception_1 != http_exception_2

    # check HTTPExceptions with different status_codes not equal
    def test_status_code_not_equal(self) -> None:  # pylint: disable=no-self-use
        message = 'HTTP Exception'
        http_exception_1 = HTTPException(status_code=400, message=message)
        http_exception_2 = HTTPException(status_code=500, message=message)
        assert http_exception_1 != http_exception_2

    # check HTTPExceptions with different messages not equal
    def test_message_not_equal(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        http_exception_1 = HTTPException(status_code=status_code, message='HTTP Exception')
        http_exception_2 = HTTPException(status_code=status_code, message='Yet Another HTTP Exception')
        assert http_exception_1 != http_exception_2


class TestHash(HttpExceptionTestCase):
    # check hash of equivalent HTTPExceptions
    def test_equivalent_http_exceptions(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        message = 'HTTP Exception'
        http_exception_1 = HTTPException(status_code=status_code, message=message)
        http_exception_2 = HTTPException(status_code=status_code, message=message)
        assert len({http_exception_1, http_exception_2}) == 1

    # check hash of HTTPException not equal to a similar HTTPExcpetion with the same fields
    def test_not_equal_to_another_class(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        message = 'HTTP Exception'
        http_exception_1 = HTTPException(status_code=status_code, message=message)
        http_exception_2 = SimilarHTTPException(status_code=status_code, message=message)
        assert len({http_exception_1, http_exception_2}) == 2

    # check hash of HTTPExceptions with different status_codes not equal
    def test_status_code_not_equal(self) -> None:  # pylint: disable=no-self-use
        message = 'HTTP Exception'
        http_exception_1 = HTTPException(status_code=400, message=message)
        http_exception_2 = HTTPException(status_code=500, message=message)
        assert len({http_exception_1, http_exception_2}) == 2

    # check hash of HTTPExceptions with different messages not equal
    def test_message_not_equal(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        http_exception_1 = HTTPException(status_code=status_code, message='HTTP Exception')
        http_exception_2 = HTTPException(status_code=status_code, message='Yet Another HTTP Exception')
        assert len({http_exception_1, http_exception_2}) == 2
