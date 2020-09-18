from fastapi import APIRouter

from ..models import BlockInfoOutput
from ..rpc import RPCNodeClient

router = APIRouter()


@router.get("/{block_hash}", response_model=BlockInfoOutput)
async def block_info(block_hash: str):
    return RPCNodeClient.block_info(block_hash)
