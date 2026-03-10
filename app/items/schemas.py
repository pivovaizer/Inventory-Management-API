from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    quantity: int = Field(default=0, ge=0)
    minimum_quantity: int = Field(default=0, ge=0)
    description: str | None = None
    category_id: int | None = None


class ItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    quantity: int | None = Field(default=None, ge=0)
    minimum_quantity: int | None = Field(default=None, ge=0)
    description: str | None = None
    category_id: int | None = None


class ItemResponse(BaseModel):
    id: int
    name: str
    quantity: int
    minimum_quantity: int
    description: str | None = None
    category_id: int | None = None

    class Config:
        from_attributes = True
