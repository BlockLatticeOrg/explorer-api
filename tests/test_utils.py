import mock
import pytest
from explorer_api.utils import Caller, rpc
from fastapi import HTTPException


class TestCaller:
    @mock.patch("explorer_api.utils.Caller._post")
    def test_call_fail(self, mock_post):
        mock_post.return_value.json.return_value = {"error": "Error message"}
        with pytest.raises(HTTPException):
            Caller.call(dict())

    @mock.patch("explorer_api.utils.Caller._post")
    def test_call(self, mock_post):
        expected_response = {"example": "value"}
        mock_post.return_value.json.return_value = expected_response
        assert Caller.call(dict()) == expected_response

    @mock.patch("httpx.post")
    def test_post(self, mock_httpx_post):
        Caller._post(data := {"key": "value"})
        mock_httpx_post.assert_called_once_with(
            Caller.uri, data=data, headers=Caller.headers
        )


class TestRPCDecorator:
    @mock.patch("explorer_api.utils.Caller.call")
    def test_rpc(self, mock_call):
        @rpc
        def f(arg):
            return arg

        f(data := {"key": "value"})
        mock_call.assert_called_once_with(data)
