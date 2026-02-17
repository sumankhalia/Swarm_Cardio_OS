from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import run_swarm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
def analyze():
    return run_swarm()
