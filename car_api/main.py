from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from calculate import calculate

class User_input(BaseModel):
    operation: str
    x: float
    y: float

app = FastAPI()


origins = [
    "http://localhost:8501",
    "http://127.0.0.1:8501/"
]

"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)"""

@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}

@app.post("/calculate")
def operate(input: User_input):
    result = calculate(input.operation, input.x, input.y)
    return result