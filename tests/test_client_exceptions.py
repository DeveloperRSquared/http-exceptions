# pylint: disable=no-self-use
import inspect

import pytest

from http_exceptions import HTTPException
from http_exceptions.client_exceptions import CLIENT_EXCEPTIONS
from http_exceptions.client_exceptions import ClientException
from http_exceptions.server_exceptions import SERVER_EXCEPTIONS
from http_exceptions.server_exceptions import ServerException
from tests.test_http_exception import HttpExceptionTestCase


class TestClientException(HttpExceptionTestCase):
    # check interface
    def test_interface(self) -> None:
        arg_spec = inspect.getfullargspec(ClientException)
        assert arg_spec.args == ['self', 'status_code', 'message']
        assert arg_spec.annotations['status_code'] == 'Optional[int]'
        assert arg_spec.annotations['message'] == 'Optional[str]'

    # check all status codes are mapped
    def test_status_codes(self) -> None:
        assert set(CLIENT_EXCEPTIONS.keys()) == set(self.client_error_status_codes)

    # check ClientException is an instance of exception
    def test_instance_of_exception(self) -> None:
        client_exception = ClientException()
        assert isinstance(client_exception, Exception)
        assert isinstance(client_exception, HTTPException)
        assert isinstance(client_exception, ClientException)


class TestCatch(HttpExceptionTestCase):
    # check that all client exceptions are caught by ServerException
    def test_catch_all_client_exceptions(self) -> None:
        for client_exception_cls in CLIENT_EXCEPTIONS.values():
            client_exception = client_exception_cls()
            try:
                raise client_exception
            except ClientException:
                pass

    # check that server exceptions are not caught by ServerException
    def test_does_not_catch_server_exceptions(self) -> None:
        for server_exception_cls in SERVER_EXCEPTIONS.values():
            server_exception = server_exception_cls()
            with pytest.raises(ServerException):
                try:
                    raise server_exception
                except ClientException:
                    pass


class TestEquality(HttpExceptionTestCase):
    # check two instances of ClientException can be equal
    def test_equivalent_client_exceptions(self) -> None:
        status_code = 500
        message = 'Client Exception'
        client_exception_1 = ClientException(status_code=status_code, message=message)
        client_exception_2 = ClientException(status_code=status_code, message=message)
        assert client_exception_1 == client_exception_2

    # check ClientExceptions with different status_codes not equal
    def test_status_code_not_equal(self) -> None:
        message = 'Client Exception'
        client_exception_1 = ClientException(status_code=400, message=message)
        client_exception_2 = ClientException(status_code=500, message=message)
        assert client_exception_1 != client_exception_2

    # check ClientExceptions with different messages not equal
    def test_message_not_equal(self) -> None:
        status_code = 500
        client_exception_1 = ClientException(status_code=status_code, message='Client Exception')
        client_exception_2 = ClientException(status_code=status_code, message='Yet Another Client Exception')
        assert client_exception_1 != client_exception_2


class TestHash(HttpExceptionTestCase):
    # check hash of two instances of ClientException can be equal
    def test_equivalent_client_exceptions(self) -> None:
        status_code = 500
        message = 'Client Exception'
        client_exception_1 = ClientException(status_code=status_code, message=message)
        client_exception_2 = ClientException(status_code=status_code, message=message)
        assert len({client_exception_1, client_exception_2}) == 1

    # check hash of ClientExceptions with different status_codes not equal
    def test_status_code_not_equal(self) -> None:
        message = 'Client Exception'
        client_exception_1 = ClientException(status_code=400, message=message)
        client_exception_2 = ClientException(status_code=500, message=message)
        assert len({client_exception_1, client_exception_2}) == 2

    # check hash of ClientExceptions with different messages not equal
    def test_message_not_equal(self) -> None:
        status_code = 500
        client_exception_1 = ClientException(status_code=status_code, message='Client Exception')
        client_exception_2 = ClientException(status_code=status_code, message='Yet Another Client Exception')
        assert len({client_exception_1, client_exception_2}) == 2
