import json

import httpx


def rpc(function):
    caller = Caller("http://157.230.53.20:7076")
    @staticmethod
    def wrapper(*args, **kwargs):
        return caller.call(function(*args, **kwargs))
    return wrapper


class Caller:
    def __init__(self, uri: str, headers: dict=None) -> None:
        self.uri = uri
        self.headers = headers or {'Content-type': 'application/json', 'Accept': 'application/json'}

    def call(self, data: dict) -> dict:
        return self._post(json.dumps(data)).json()

    def _post(self, data: str) -> httpx.Response:
        return httpx.post(self.uri, data=data, headers=self.headers)


class RPCNodeClient:
    @rpc
    def account_history(account: str, page: int=0, count: int=100) -> dict:
        return {
            "action": "account_history",
            "account": account,
            "count": count,
            "offset": count * page,
        }

    @rpc
    def account_info(account: str, representative: bool=True, weight: bool=True, pending: bool=True) -> dict:
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
    def pending(account: str, count: int=100, source: bool=True) -> dict:
        return {
            "action": "pending",
            "account": account,
            "count": count,
            "source": source,
        }
