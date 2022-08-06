from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from medical_expert import *

class Symptom(BaseModel):
    name: str
    value: str

    def getReport(self): 
        return SymptomModel[self.value]

class PhisicalExploration(BaseModel):
    name: str
    value: str

    def getReport(self): 
        return PhysicalExplorationModel[self.value]

class Disorder(BaseModel):
    name: str
    value: str

    def getReport(self): 
        return DisorderModel[self.value]

class Study(BaseModel):
    name: str
    value: str

    def getReport(self): 
        return StudyModel[self.value]

class Report(BaseModel):
    symptom: Symptom
    physical_exploration: PhisicalExploration
    disorder: Disorder
    study: Study


app = FastAPI()


@app.get("/ping")
def read_root():
    return "Pong"


@app.post("/diagnostics")
def read_item(report: Report):
    new_diagnostic()
    engine = MedicalRobot()
    engine.reset()
    engine.declare(Fact(SymptomModel.TS), Fact(SymptomModel.MA), Fact(SymptomModel.F), Fact(SymptomModel.DG), Fact(StudyModel.HCA))
    engine.run()
    return diagnostic.result