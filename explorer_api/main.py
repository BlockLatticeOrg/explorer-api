from fastapi import FastAPI

from . import __version__
from .routers import accounts, blocks

app = FastAPI(docs_url=False, redoc_url=False)

v1 = FastAPI(
    title="BlockLattice.org Explorer API",
    version=__version__,
)

v1.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
v1.include_router(blocks.router, prefix="/blocks", tags=["blocks"])

app.mount("/v1", v1)
