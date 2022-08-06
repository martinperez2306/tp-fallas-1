from fastapi import FastAPI
from typing import Union
from typing import List
from pydantic import BaseModel
from medical_expert import *
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",   
]

class Symptom:
    def __init__(self, value):
        self.value = value

    def getReport(self): 
        return SymptomModel[self.value]

class PhisicalExploration:
    def __init__(self, value):
        self.value = value

    def getReport(self): 
        return PhysicalExplorationModel[self.value]

class Disorder:
    def __init__(self, value):
        self.value = value

    def getReport(self): 
        return DisorderModel[self.value]

class Study:
    def __init__(self, value):
        self.value = value

    def getReport(self): 
        return StudyModel[self.value]

class Report(BaseModel):
    symptoms: List[str]
    physical_explorations: List[str]
    disorders: List[str]
    studies: List[str]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "UP", "description": "MIS - Medical Intelligent Server"}

@app.get("/ping")
def read_root():
    return "Pong"


@app.post("/diagnostics")
def read_item(report: Report):
    new_diagnostic()
    engine = MedicalRobot()
    engine.reset()
    symptom_facts = []
    physical_exploration_facts = []
    disorder_facts = []
    study_facts = []

    for symptom_value in report.symptoms: 
        symptom = Symptom(symptom_value)
        symptom_facts.append(Fact(symptom.getReport()))

    for physical_exploration_value in report.physical_explorations: 
        physical_exploration = PhisicalExploration(physical_exploration_value)
        physical_exploration_facts.append(Fact(physical_exploration.getReport()))

    for disorder_value in report.disorders: 
        disorder = Disorder(disorder_value)
        disorder_facts.append(Fact(disorder.getReport()))

    for study_value in report.studies: 
        study = Study(study_value)
        study_facts.append(Fact(study.getReport()))

    if symptom_facts: 
        engine.declare(*symptom_facts)
    if physical_exploration_facts:
            engine.declare(*physical_exploration_facts)
    if disorder_facts:
        engine.declare(*disorder_facts)
    if study_facts:
        engine.declare(*study_facts)
    
    engine.run()
    return {"result": diagnostic.result}