from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    minimum_quantity = Column(Integer, default=0)
    description = Column(String, nullable=True)
