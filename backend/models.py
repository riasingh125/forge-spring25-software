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
    country: str
    zip_code: str

class Weights(BaseModel):
    affordability: int
    health_concerns: int
    essential_services: int
    plan_flexibility: int
    geographic_coverage: int
    dependencies: int
    convenience: int
    long_term_benefits: int

# Main Pydantic format for JSON
class UserInputForm(BaseModel):
    first_name: str
    last_name: str
    age: int
    income: float
    budget: float
    coverage: Coverage
    contact: Contact
    address: Address
    weights: Weights