from fastapi import APIRouter

from .. import rpc
from ..models import BlockInfoOutput

router = APIRouter()


@router.get("/{block_hash}", response_model=BlockInfoOutput)
async def block_info(block_hash: str):
    return rpc.block_info(block_hash)
