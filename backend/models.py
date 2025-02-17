from pydantic import BaseModel
from typing import List


# Format for messages sent - a single string
class ChatBotMessage(BaseModel):
    message: str








class Coverage(BaseModel):
    ages_of_people_needing_coverage: List[int]
    personal_health_concerns: str
    budget: float

class Contact(BaseModel):
    email: str
    number: int

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Weights(BaseModel):
    age: int
    income: int
    city: int

# Main Pydantic format for JSON
class UserInputForm(BaseModel):
    insurance_id: int
    age: int
    income: float
    budget: float
    coverage: Coverage
    contact: Contact
    address: Address
    weights: Weights