from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# To run app:
# fastapi dev root.py

# Format for messages sent - a single string
class ChatBotMessage(BaseModel):
    message: str


@app.get("/")
def root():
    return {"Hello": "World"}


# ===========================
# ChatBot
# ===========================

# Endpoint for sending a message to chatbot and receiving response
# 'data' parameter corresponds to JSON body in POST request
@app.post("/chat/message")
async def send_message(data: ChatBotMessage):
    return {"received": data.message, "response": "hi"}


# ===========================
# User Form Input / Results
# ===========================

# Format for user form input
class UserInputForm(BaseModel):
    firstName: str
    lastName: str
    email: str
    city: str
    state: str
    zip: str
    country: str
    salary: float
    numHousehold: int
    budget: float
    concerns: str | None = None  # Optional field

# Endpoint for sending user input from form
# 'data' parameters corresponds to JSON body in POST request
@app.post("/form/send")
def send_form(data: UserInputForm):
    return {"message": "Form received", "data": data.dict()}

# getting results
@app.get("/results")
async def get_results():
    return {
        "best_insurance_options": [
            {"name": "Plan A", "price": "$100"},
            {"name": "Plan B", "price": "$200"},
            {"name": "Plan C", "price": "$300"}
        ]
    }
