from typing import Dict, List, Optional

from pydantic import BaseModel, validator


class HistoryModel(BaseModel):
    type: str
    account: str
    amount: int
    local_timestamp: int
    height: int
    hash: str


class AccountHistoryOutput(BaseModel):
    account: str
    history: Optional[List[HistoryModel]]
    previous: Optional[str]

    @validator("history", pre=True, always=True)
    def validate_history(cls, value):
        return [] if not value else value


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
    destination: Optional[str]
    previous: Optional[str]
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
    source: Optional[str]


class PendingOutput(BaseModel):
    blocks: Dict[str, BlockPendingModel]
