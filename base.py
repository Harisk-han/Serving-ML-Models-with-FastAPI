# Input schema (must match model training)
from pydantic import BaseModel, Field

class Passenger(BaseModel):
    Pclass: int = Field(..., ge=1, le=3)
    Sex: int = Field(..., ge=0, le=1)  # 0 = male, 1 = female
    Age: float = Field(..., ge=0)
    Fare: float = Field(..., ge=0)
