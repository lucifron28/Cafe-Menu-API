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













