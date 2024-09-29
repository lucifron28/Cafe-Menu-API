from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_available: bool
    category: str  # "pastry" or "coffee"
    description: Optional[str] = None

items = [
    Item(id=1, name="Croissant", price=2.5, is_available=True, category="pastry", description="A buttery, flaky, and delicious croissant."),
    Item(id=2, name="Muffin", price=3.0, is_available=True, category="pastry", description="A soft and moist muffin with blueberries."),
    Item(id=3, name="Bagel", price=1.5, is_available=True, category="pastry", description="A chewy bagel with sesame seeds."),
    Item(id=4, name="Espresso", price=2.0, is_available=True, category="coffee", description="A strong and rich espresso shot."),
    Item(id=5, name="Latte", price=3.5, is_available=True, category="coffee", description="A smooth and creamy latte."),
    Item(id=6, name="Cappuccino", price=3.0, is_available=True, category="coffee", description="A frothy cappuccino with a sprinkle of cocoa."),
    Item(id=7, name="Americano", price=2.5, is_available=True, category="coffee", description="A bold and robust americano."),
    Item(id=8, name="Donut", price=1.0, is_available=True, category="pastry", description="A classic glazed donut."),
    Item(id=9, name="Scone", price=2.0, is_available=True, category="pastry", description="A crumbly scone with raisins."),
    Item(id=10, name="Macchiato", price=3.0, is_available=True, category="coffee", description="A rich macchiato with a touch of foam.")
]

@app.get("/menu", response_model=List[Item])
def get_items():
    return items

@app.get("/menu/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/menu/category/{category_name}", response_model=List[Item])
def get_items_by_category(category_name: str):
    items_by_category = []
    for item in items:
        if item.category == category_name:
            items_by_category.append(item)
    return items_by_category

@app.post("/menu", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/menu/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.patch("/menu/{item_id}", response_model=Item)
def patch_item(item_id: int, item_update: Item):
    for item in items:
        if item.id == item_id:
            if item_update.name is not None:
                item.name = item_update.name
            if item_update.price is not None:
                item.price = item_update.price
            if item_update.is_available is not None:
                item.is_available = item_update.is_available
            if item_update.category is not None:
                item.category = item_update.category
            if item_update.description is not None:
                item.description = item_update.description
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/menu/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            return items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")