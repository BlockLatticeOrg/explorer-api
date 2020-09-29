import mock
import pytest
from explorer_api import utils
from fastapi import HTTPException


class TestCaller:
    @mock.patch("explorer_api.utils.Caller._post")
    def test_call_fail(self, mock_post):
        mock_post.return_value.json.return_value = {"error": "Error message"}
        with pytest.raises(HTTPException):
            utils.Caller.call(dict())

    @mock.patch("explorer_api.utils.Caller._post")
    def test_call(self, mock_post):
        expected_response = {"example": "value"}
        mock_post.return_value.json.return_value = expected_response
        assert utils.Caller.call(dict()) == expected_response


class TestRPCDecorator:
    @mock.patch("explorer_api.utils.Caller.call")
    def test_rpc(self, mock_call):
        @utils.rpc
        def f(arg):
            return arg

        f(data := {"key": "value"})
        mock_call.assert_called_once_with(data)
