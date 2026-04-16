from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


app=FastAPI()

model=joblib.load('my_trained_model.pkl')

class StudentData(BaseModel):
    reading_score: float
    writing_score: float
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str


@app.post("/predict")   
def predict(data:StudentData):
     new_data = pd.DataFrame({
        'reading score': [data.reading_score],
        'writing score': [data.writing_score],
        'gender': [data.gender],
        'race/ethnicity': [data.race_ethnicity],
        'parental level of education': [data.parental_level_of_education],
        'lunch': [data.lunch],
        'test preparation course': [data.test_preparation_course]
    })
     prediction = model.predict(new_data)
     return {
        "predicted_math_score": float(prediction[0])
    }
