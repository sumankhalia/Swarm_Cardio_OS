from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import run_swarm

app = FastAPI()

# ✅ ADD THIS BLOCK 🔥
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For dev/demo (later restrict)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Swarm Cardio OS Running"}

@app.get("/analyze")
def analyze():
    return run_swarm()
