import json

import httpx
from fastapi import HTTPException
from prettyconf import config


def rpc(function):
    @staticmethod
    def wrapper(*args, **kwargs):
        return Caller.call(function(*args, **kwargs))

    return wrapper


class Caller:
    uri = config("NANO_NODE_URL")
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


class RPCNodeClient:
    @rpc
    def account_history(account: str, page: int = 0, count: int = 100) -> dict:
        return {
            "action": "account_history",
            "account": account,
            "count": count,
            "offset": count * page,
        }

    @rpc
    def account_info(
        account: str,
        representative: bool = True,
        weight: bool = True,
        pending: bool = True,
    ) -> dict:
        return {
            "action": "account_info",
            "account": account,
            "representative": representative,
            "weight": weight,
            "pending": pending,
        }

    @rpc
    def block_info(_hash: str) -> dict:
        return {
            "action": "block_info",
            "json_block": True,
            "hash": _hash,
        }

    @rpc
    def delegators(account: str) -> dict:
        return {
            "action": "delegators",
            "account": account,
        }

    @rpc
    def pending(account: str, count: int = 100, source: bool = True) -> dict:
        return {
            "action": "pending",
            "account": account,
            "count": count,
            "source": source,
        }
