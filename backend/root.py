from fastapi import FastAPI, status
from pydantic import BaseModel

from models import UserInputForm, ChatBotMessage
from rankings import RankingLogic

from models import UserInputForm
from models import ChatBotMessage

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
# cd backend
# fastapi dev root.py




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


# Endpoint for sending user input from form
# 'data' parameters corresponds to JSON body in POST request
@app.post("/form/send")
async def send_form(data: UserInputForm):
    # Adds more stuff to actually recommend.

    # form_data = data.model_dump()
    #
    # weights = {k: v for k, v in form_data.items() if "weight" in k}
    #
    # ranking = RankingLogic(weights, form_data['insurance_id'])
    # ranking.ranking_logics()
    # ranking.pair_keys()
    # total_score = ranking.total_scores()

    #print(data)
    return {"total_score": 100}

@app.post("/form/upload-file")
async def send_form():



# getting results
@app.get("/results")
async def get_results():
    return {
        "results": [
            {"name": "Plan A", "price": "$100"},
            {"name": "Plan B", "price": "$200"},
            {"name": "Plan C", "price": "$300"}
        ]
    }