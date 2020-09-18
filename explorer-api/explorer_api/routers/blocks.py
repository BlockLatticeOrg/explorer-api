from fastapi import APIRouter

from explorer_api.models import BlockInfoOutput
from explorer_api.rpc import RPCNodeClient

router = APIRouter()


@router.get("/{block_hash}", response_model=BlockInfoOutput)
async def block_info(block_hash: str):
    return RPCNodeClient.block_info(block_hash)
