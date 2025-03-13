from typing import Any, List, Optional

from pydantic import BaseModel

from datetime import date


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[float]
    
class DataInputSchema(BaseModel):
    dteday: Optional[str]  # Date column
    season: Optional[str]  # Categorical (object)
    hr: Optional[str]  # Categorical (object)
    holiday: Optional[str]  # Categorical (object)
    weekday: Optional[str]  # Categorical (object) - has missing values
    workingday: Optional[str]  # Categorical (object)
    weathersit: Optional[str]  # Categorical (object) - has missing values
    temp: Optional[float]  # Continuous numeric
    atemp: Optional[float]  # Continuous numeric
    hum: Optional[float]  # Continuous numeric
    windspeed: Optional[float]  # Continuous numeric
    casual: Optional[int]  # Integer
    registered: Optional[int]  # Integer



class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

