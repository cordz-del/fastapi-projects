from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="FastAPI Project Demo",
    description="An example API showcasing FastAPI for building cloud-ready services.",
    version="1.0.0"
)

# Pydantic models for data validation
class PredictionRequest(BaseModel):
    features: List[float]

class PredictionResponse(BaseModel):
    prediction: float

# Dummy model function for demonstration (e.g., summing input features)
def dummy_predict(features: List[float]) -> float:
    return sum(features)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the FastAPI Project Demo!"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict(request: PredictionRequest):
    if not request.features:
        raise HTTPException(status_code=400, detail="Features list cannot be empty")
    pred = dummy_predict(request.features)
    return PredictionResponse(prediction=pred)
