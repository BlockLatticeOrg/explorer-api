from fastapi import APIRouter

from ..models import BlockInfoOutput
from .. import rpc

router = APIRouter()


@router.get("/{block_hash}", response_model=BlockInfoOutput)
async def block_info(block_hash: str):
    return rpc.block_info(block_hash)
