from typing import Optional

from fastapi import APIRouter

from ..models import (
    AccountHistoryOutput,
    AccountInfoOutput,
    DelegatorsOutput,
    PendingOutput,
)
from . import rpc

router = APIRouter()


@router.get("/{account}/history", response_model=AccountHistoryOutput)
async def account_history(
    account: str, page: Optional[int] = 0, count: Optional[int] = 100
):
    return rpc.account_history(account, page=page, count=count)


@router.get("/{account}/info", response_model=AccountInfoOutput)
async def account_info(
    account: str,
    representative: Optional[bool] = True,
    weight: Optional[bool] = True,
    pending: Optional[bool] = True,
):
    return rpc.account_info(
        account, representative=representative, weight=weight, pending=pending
    )


@router.get("/{account}/delegators", response_model=DelegatorsOutput)
async def delegators(account: str):
    return rpc.delegators(account)


@router.get("/{account}/pending", response_model=PendingOutput)
async def pending(
    account: str, count: Optional[int] = 100, source: Optional[bool] = True
):
    return rpc.pending(account, count=count, source=source)
