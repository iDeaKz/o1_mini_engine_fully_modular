from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict, Optional

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., example="Sword")
    description: str = Field(..., example="A sharp blade.")
    price: float = Field(..., gt=0, example=100.0)

class ItemDatabase:
    def __init__(self) -> None:
        self.items: Dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        self.items[item.name] = item

    def get_item(self, name: str) -> Optional[Item]:
        return self.items.get(name)

def get_item_database() -> ItemDatabase:
    return item_db

item_db = ItemDatabase()

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item, db: ItemDatabase = Depends(get_item_database)) -> Item:
    if db.get_item(item.name):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item already exists")
    db.add_item(item)
    return item

@app.get("/items/{item_name}", response_model=Item)
async def get_item(item_name: str, db: ItemDatabase = Depends(get_item_database)) -> Item:
    item = db.get_item(item_name)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item
