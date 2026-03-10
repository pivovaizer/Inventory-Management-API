from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.items.router import router as items_router
from app.auth.router import router as auth_router
from app.core.logging_config import get_logger
import app.models


logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Inventory Management API started")
    yield
    logger.info("Inventory Management API stopped")


app = FastAPI(title="Inventory Management API", lifespan=lifespan)

app.include_router(items_router)
app.include_router(auth_router)
