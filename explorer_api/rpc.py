from .utils import rpc_call


class RPCNodeClient:
    @rpc_call
    def account_history(account: str, page: int = 0, count: int = 100) -> dict:
        return {
            "action": "account_history",
            "account": account,
            "count": count,
            "offset": count * page,
        }

    @rpc_call
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

    @rpc_call
    def block_info(_hash: str) -> dict:
        return {
            "action": "block_info",
            "json_block": True,
            "hash": _hash,
        }

    @rpc_call
    def delegators(account: str) -> dict:
        return {
            "action": "delegators",
            "account": account,
        }

    @rpc_call
    def pending(account: str, count: int = 100, source: bool = True) -> dict:
        return {
            "action": "pending",
            "account": account,
            "count": count,
            "source": source,
        }
