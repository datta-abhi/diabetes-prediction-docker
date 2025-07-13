from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# initialise fastapi
app = FastAPI()

# load model
with open("model.pkl",'rb') as f:
    model = pickle.load(f)
    
# Create input Schema as Pydantic Model
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float
    
@app.post("/predict")
def predict(data: DiabetesInput):
    
    input_array = np.array([
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]).reshape(1,-1)
    
    prediction = model.predict(input_array)[0]
    
    return {"prediction": int(prediction)}   