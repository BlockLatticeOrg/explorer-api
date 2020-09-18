from fastapi import FastAPI

from routers import accounts, blocks

app = FastAPI()


app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
app.include_router(blocks.router, prefix="/blocks", tags=["blocks"])
