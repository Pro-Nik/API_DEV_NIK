from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI(
title="My First FastAPI App",
description="This is a simple FastAPI application for learning purposes.",
version="1.0.0"
)
class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def home():
    return {"Hello "}

@app.get("/about")
def about():
    return {"This is the about page"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}


