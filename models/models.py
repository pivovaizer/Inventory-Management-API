from sqlalchemy import Column, Integer, String
from db.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    minimum_quantity = Column(Integer, default=0)
    description = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

