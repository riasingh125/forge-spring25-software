from pydantic import BaseModel, Field, constr
from typing import List


# Format for messages sent - a single string
class ChatBotMessage(BaseModel):
    message: str



class Coverage(BaseModel):
    ages_of_Dependencies: List[int] = Field(..., alias="agesOfDependencies")
    personal_health_concerns: str = Field(..., alias="personalHealthConcerns")
    budget: float = Field(..., ge = 0) # Should have to be greater than 0 ?

class Contact(BaseModel):
    email: str
    number: str

class Address(BaseModel):
    city: str
    state: str
    country: str
    zip_code: str = Field(..., alias="zipCode")

class Weights(BaseModel):
    affordability: int = Field(..., ge=0, le=10)
    health_concerns: int = Field(..., ge=0, le=10, alias="healthConcerns")
    essential_services: int = Field(..., ge=0, le=10, alias="essentialServices")
    plan_flexibility: int = Field(..., ge=0, le=10, alias="planFlexibility")
    geographic_coverage: int = Field(..., ge=0, le=10, alias="geographicCoverage")
    dependencies: int = Field(..., ge=0, le=10)
    convenience: int = Field(..., ge=0, le=10)
    long_term_benefits: int= Field(..., ge=0, le=10, alias="longTermBenefits")

# Main Pydantic format for JSON
class UserInputForm(BaseModel):
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    age: int
    income: float
    budget: float
    coverage: Coverage
    contact: Contact
    address: Address
    weights: Weights