from pydantic import BaseModel
from typing import Literal

class Customer(BaseModel):
    age: int
    gender: Literal['male', 'female']
    bmi: float 
    children: int
    smoker: Literal['yes', 'no']  
    region: Literal['northeast', 'southwest', 'northwest', 'southeast']
    medical_history: Literal['Heart disease', 'High blood pressure', 'Diabetes', None]
    family_medical_history: Literal['Heart disease', 'High blood pressure', 'Diabetes', None]
    exercise_frequency: Literal['Rarely', 'Occasionally', 'Frequently', 'Never']    
    occupation: Literal['Unemployed',  'Student', 'Blue collar', 'White collar']
    coverage_level: Literal['Basic', 'Standard', 'Premium']