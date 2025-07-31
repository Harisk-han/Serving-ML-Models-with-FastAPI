from fastapi import FastAPI
from base import Passenger
import numpy as np

app = FastAPI()

@app.post("/predict")
def predict(passenger: Passenger):
    features = np.array([[passenger.Pclass, passenger.Sex, passenger.Age, passenger.Fare]])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features).max()
    return {
        "prediction": int(prediction),  # 0 = Died, 1 = Survived
        "confidence": round(confidence, 2)
    }
import joblib
model = joblib.load("titanic_model.joblib")
