from fastapi import FastAPI
from typing import Union


app = FastAPI()


@app.get("/ping")
def read_root():
    return "Pong"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}