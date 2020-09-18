from fastapi import FastAPI

from . import __version__
from .routers import accounts, blocks

app = FastAPI(
    title="BlockLattice.org Explorer API",
    version=__version__,
)


app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
app.include_router(blocks.router, prefix="/blocks", tags=["blocks"])
