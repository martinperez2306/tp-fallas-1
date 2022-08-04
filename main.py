from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

class Report(BaseModel):
    symptom: str
    physical_exploration: str
    disorders: str
    study: str

app = FastAPI()


@app.get("/ping")
def read_root():
    return "Pong"


@app.post("/diagnostics")
def read_item(report: Report):
    return report