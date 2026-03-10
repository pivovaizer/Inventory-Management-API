from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.items.router import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Inventory Management API", lifespan=lifespan)

app.include_router(items_router)
