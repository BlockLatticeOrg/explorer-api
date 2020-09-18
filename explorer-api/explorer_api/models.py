from typing import List, Dict

from pydantic import BaseModel


class HistoryModel(BaseModel):
    type: str
    account: str
    amount: int
    local_timestamp: int
    height: int
    hash: str


class AccountHistoryOutput(BaseModel):
    account: str
    history: List[HistoryModel]
    previous: str = None


class AccountInfoOutput(BaseModel):
    account_version: int
    balance: int
    block_count: int
    confirmation_height: int
    confirmation_height_frontier: str
    frontier: str
    modified_timestamp: int
    open_block: str
    pending: int
    representative: str
    representative_block: str
    weight: int


class BlockInfoContentModel(BaseModel):
    balance: str
    destination: str = None
    previous: str = None
    signature: str


class BlockInfoOutput(BaseModel):
    amount: int
    balance: int
    block_account: str
    confirmed: bool
    contents: BlockInfoContentModel
    height: int
    local_timestamp: int


class DelegatorsOutput(BaseModel):
    delegators: Dict[str, int]


class BlockPendingModel(BaseModel):
    amount: int
    source: str = None


class PendingOutput(BaseModel):
    blocks: Dict[str, BlockPendingModel]
