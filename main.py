from fastapi import FastAPI
from db.database import init_db
from routers.item import router as item_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Inventory Management API", lifespan=lifespan)

app.include_router(item_router)
