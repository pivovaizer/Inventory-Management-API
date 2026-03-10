from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import Item
from schemas.item import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

# GET /items - Retrieve all items
@router.get("/", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

# GET /items/to_buy - Retrieve items that need to be bought (quantity < minimum_quantity)
@router.get("/to_buy", response_model=list[ItemResponse])
def get_items_to_buy(db: Session = Depends(get_db)):
    return db.query(Item).filter(Item.quantity < Item.minimum_quantity).all()

# POST /items - Create a new item
@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump()) # Convert Pydantic model to SQLAlchemy model
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# PUT /items/{item_id} - Update an existing item
@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item.model_dump(exclude_unset=True).items(): # Update only provided fields
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# DELETE /items/{item_id} - Delete an item
@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {'detail': 'Item deleted successfully'}


# PATCH /items/{item_id}/adjust - Update only the quantity of an item
@router.patch("/{item_id}/adjust", response_model=ItemResponse)
def adjust_item_quantity(item_id: int, quantity: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.quantity = quantity
    db.commit()
    db.refresh(db_item)
    return db_item
