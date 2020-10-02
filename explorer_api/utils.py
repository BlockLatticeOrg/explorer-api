import json

import httpx
from fastapi import HTTPException

from . import settings


def rpc(function):
    def wrapper(*args, **kwargs):
        return Caller.call(function(*args, **kwargs))

    return wrapper


class Caller:
    uri = settings.NANO_NODE_URL
    headers = {"Content-type": "application/json", "Accept": "application/json"}

    @classmethod
    def call(cls, data: dict) -> dict:
        response = cls._post(json.dumps(data)).json()
        if error := response.get("error"):
            raise HTTPException(status_code=400, detail=error)
        return response

    @classmethod
    def _post(cls, data: str) -> httpx.Response:
        return httpx.post(cls.uri, data=data, headers=cls.headers)
