from pydantic import BaseModel


class ItemCreate(BaseModel):
    category: str
    name: str
    quantity: int = 0
    minimum_quantity: int = 0
    description: str | None = None


class ItemUpdate(BaseModel):
    category: str | None = None
    name: str | None = None
    quantity: int | None = None
    minimum_quantity: int | None = None
    description: str | None = None


class ItemResponse(BaseModel):
    id: int
    category: str
    name: str
    quantity: int
    minimum_quantity: int
    description: str | None = None

    class Config:
        from_attributes = True
