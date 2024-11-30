from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel
from typing import List, Optional
from logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str
    price: float

# CRUD Operations
@router.get("/items/", response_model=List[Item])
async def get_items(skip: int = 0, limit: int = 10, q: Optional[str] = Query(None)):
    logger.info("Fetching items")
    return [{"name": "Sword", "description": "A sharp blade", "price": 150.0}][skip : skip + limit]

@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    logger.info(f"Creating item: {item.name}")
    return item

@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    logger.info(f"Updating item {item_id} with data: {item.dict()}")
    return item

@router.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    logger.info(f"Deleting item {item_id}")
    return {"message": f"Item {item_id} deleted"}
    
# Batch Operations Example
@router.post("/items/batch", response_model=List[Item])
async def create_items(items: List[Item]):
    logger.info(f"Creating batch of {len(items)} items")
    return items
