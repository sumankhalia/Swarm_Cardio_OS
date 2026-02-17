from fastapi import FastAPI
from main import run_swarm

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Swarm Cardio OS Running"}


@app.get("/analyze")
def analyze():
    return run_swarm()
