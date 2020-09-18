from typing import List, Dict

from pydantic import BaseModel


class AccountHistoryInput(BaseModel):
    account: str
    page: int = 0
    count: int = 100


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
    previous: str


class AccountInfoInput(BaseModel):
    account: str
    representative: bool = True
    weight: bool = True
    pending: bool = True


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


class BlockInfoInput(BaseModel):
    hash: str


class BlockInfoContentModel(BaseModel):
    balance: str
    destination: str
    previous: str
    signature: str


class BlockInfoOutput(BaseModel):
    amount: int
    balance: int
    block_account: str
    confirmed: bool
    contents: BlockInfoContentModel
    height: int
    local_timestamp: int


class DelegatorsInput(BaseModel):
    account: str


class DelegatorsOutput(BaseModel):
    delegators: Dict[str, int]


class PendingInput(BaseModel):
    account: str
    count: int = 100
    source: bool = True


class BlockPendingModel(BaseModel):
    amount: int
    source: str = None


class PendingOutput(BaseModel):
    blocks: Dict[str, BlockPendingModel]
