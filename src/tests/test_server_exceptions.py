import pytest

from http_exceptions import HTTPException
from http_exceptions.client_exceptions import CLIENT_EXCEPTIONS
from http_exceptions.client_exceptions import ClientException
from http_exceptions.server_exceptions import SERVER_EXCEPTIONS
from http_exceptions.server_exceptions import ServerException
from tests.test_http_exception import HttpExceptionTestCase


class TestServerException(HttpExceptionTestCase):
    # check all status codes are mapped
    def test_status_codes(self) -> None:
        assert set(SERVER_EXCEPTIONS.keys()) == set(self.server_error_status_codes)

    # check ServerException is an instance of exception
    def test_instance_of_exception(self) -> None:  # pylint: disable=no-self-use
        server_exception = ServerException()
        assert isinstance(server_exception, Exception)
        assert isinstance(server_exception, HTTPException)
        assert isinstance(server_exception, ServerException)


class TestCatch(HttpExceptionTestCase):
    # check that all server exceptions are caught by ServerException
    def test_catch_all_server_exceptions(self) -> None:  # pylint: disable=no-self-use
        for server_exception_cls in SERVER_EXCEPTIONS.values():
            server_exception = server_exception_cls()
            try:
                raise server_exception
            except ServerException:
                pass

    # check that client exceptions are not caught by ServerException
    def test_does_not_catch_client_exceptions(self) -> None:  # pylint: disable=no-self-use
        for client_exception_cls in CLIENT_EXCEPTIONS.values():
            client_exception = client_exception_cls()
            with pytest.raises(ClientException):
                try:
                    raise client_exception
                except ServerException:
                    pass


class TestEquality(HttpExceptionTestCase):
    # check two instances of ServerException can be equal
    def test_equivalent_server_exceptions(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        message = 'Server Exception'
        server_exception_1 = ServerException(status_code=status_code, message=message)
        server_exception_2 = ServerException(status_code=status_code, message=message)
        assert server_exception_1 == server_exception_2

    # check ServerExceptions with different status_codes not equal
    def test_status_code_not_equal(self) -> None:  # pylint: disable=no-self-use
        message = 'Server Exception'
        server_exception_1 = ServerException(status_code=400, message=message)
        server_exception_2 = ServerException(status_code=500, message=message)
        assert server_exception_1 != server_exception_2

    # check ServerExceptions with different messages not equal
    def test_message_not_equal(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        server_exception_1 = ServerException(status_code=status_code, message='Server Exception')
        server_exception_2 = ServerException(status_code=status_code, message='Yet Another Server Exception')
        assert server_exception_1 != server_exception_2


class TestHash(HttpExceptionTestCase):
    # check hash of two instances of ServerException can be equal
    def test_equivalent_server_exceptions(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        message = 'Server Exception'
        server_exception_1 = ServerException(status_code=status_code, message=message)
        server_exception_2 = ServerException(status_code=status_code, message=message)
        assert len({server_exception_1, server_exception_2}) == 1

    # check hash of ServerExceptions with different status_codes not equal
    def test_status_code_not_equal(self) -> None:  # pylint: disable=no-self-use
        message = 'Server Exception'
        server_exception_1 = ServerException(status_code=400, message=message)
        server_exception_2 = ServerException(status_code=500, message=message)
        assert len({server_exception_1, server_exception_2}) == 2

    # check hash of ServerExceptions with different messages not equal
    def test_message_not_equal(self) -> None:  # pylint: disable=no-self-use
        status_code = 500
        server_exception_1 = ServerException(status_code=status_code, message='Server Exception')
        server_exception_2 = ServerException(status_code=status_code, message='Yet Another Server Exception')
        assert len({server_exception_1, server_exception_2}) == 2
