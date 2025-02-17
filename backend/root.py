from fastapi import FastAPI, status
from pydantic import BaseModel
from rankings import RankingLogic
app = FastAPI()


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

# Endpoint for sending user input from form
# 'data' parameters corresponds to JSON body in POST request
@app.post("/form/send")
async def send_form(data):
    # Adds more stuff to actually recommend.
    form_data = data.model_dump()

    weights = {k: v for k, v in form_data.items() if "weight" in k}

    ranking = RankingLogic(weights, form_data['insurance_id'])
    ranking.ranking_logics()
    ranking.pair_keys()
    total_score = ranking.total_scores()

    return {"total_score": total_score}

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