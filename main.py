from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from medical_expert import *

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
    new_diagnostic()
    engine = MedicalRobot()
    engine.reset()
    engine.declare(ReportModel(tos='TS'), ReportModel(congestion='MA'), ReportModel(fiebre='F'))
    engine.run()
    return diagnostic.result