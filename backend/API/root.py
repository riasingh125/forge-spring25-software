from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from .PlanSummaries import PlanSummaries
from ..RankingLogics.rankings import WeightedPlanRanking
from ..API.models import UserInputForm
from ..API.models import ChatBotMessage
import json

# import function to upload files to s3
from .upload_extract import upload_and_extract
# import function to get chatbot response
from ..Chatbot.chatbot import get_chatbot_response
import asyncio

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=["http://localhost:5173"],
    # Allow frontend in React to connect
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# To run app:
# cd backend
# fastapi dev root.py

history = {}


@app.get("/")
def root():
    return {"FastAPI Running!!!!!"}


@app.post("/chat/message")
async def send_message(data: ChatBotMessage):
    response = get_chatbot_response(data.message, history)
    return {"received": data.message, "response": response}


@app.post("/form/submit")
async def upload_pdfs(form_data: str = Form(...),
                      files: List[UploadFile] = File(...)):
    # Process form data into dictionary
    form_dict = json.loads(form_data)

    # Check against Pydantic Model
    user_input = UserInputForm(**form_dict)
    user_input = user_input.model_dump()

    # check files for right type:
    for file in files:
        if file.content_type != 'application/pdf':
            return {"error": "file is not of type pdf"}

    plans = {}
    premiums = user_input['premium']
    for i, j in zip(premiums, files):
        plans[j] = i

    # upload to s3 and textract
    # { "name": filename, "text": "TEXT RESULTS " }
    results = await upload_and_extract(plans)

    # The weights:
    weight = user_input['weights']
    del user_input['weights']

    coverage = user_input['coverage']
    location = user_input['address']

    user_input['health_concerns'] = coverage['personal_health_concerns']
    user_input['budget'] = coverage['budget']
    user_input['zip_code'] = location['zip_code']
    user_input['city'] = location['city']
    user_input['state'] = location['state']
    user_input['household_size'] = coverage['household_size']
    user_input['individual_bool'] = (coverage['household_size'] == 1)

    weights = {k: v / 10 for k, v in weight.items()}

    # The premiums:
    async def process_plan(plan_name: str, plan_content: str,
                           plan_premium: float):
        ranking_instance = WeightedPlanRanking(weights, plan_content,
                                               user_input, plan_premium,
                                               user_input['individual_bool'])
        unweighted_scores = await ranking_instance.ranking_logics()
        weighted_scores = ranking_instance.pair_keys()
        total_score = ranking_instance.total_scores()
        summary = PlanSummaries(plan_content, user_input['age'],
                                user_input['budget'], user_input['individual_bool'])
        short_summary = await summary.get_short_summary()
        return plan_name, unweighted_scores, weighted_scores, total_score, short_summary, plan_content

    tasks = [process_plan(name, content[0], content[1]) for name, content in
             results.items()]

    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)

    to_frontend = []

    # Store the results in the history
    for name, unweighted_scores, weighted_scores, total_score, short_summary, plan_content in results:
        # {'file_name': 'weighted_scores: dict, 'total_score': float, 'text': str}
        history[name] = {
            "weighted_scores": weighted_scores,
            "total_score": total_score,
            "text": plan_content
        }

        to_frontend.append({
            "name": name,
            "weightedScores": unweighted_scores,
            "totalScore": total_score,
            "shortSummary": short_summary
        })

    return to_frontend
