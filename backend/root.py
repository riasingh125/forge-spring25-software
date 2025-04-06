from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from rankings import WeightedPlanRanking
from models import UserInputForm
from models import ChatBotMessage
import json

# import function to upload files to s3
from upload_extract import upload_and_extract
# import function to get chabot response
# from chatbot import get_chatbot_response
import asyncio

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5173"],
	# Allow frontend in React to conncet
	allow_credentials=True,
	allow_methods=["*"],  # Allow all methods
	allow_headers=["*"],  # Allow all headers
)

# To run app:
# cd backend
# fastapi dev root.py

history = {}
to_frontend = {}


@app.get("/")
def root():
	return {"FastAPI Running!!!!!"}


@app.post("/chat/message")
async def send_message(data: ChatBotMessage):
	# response = get_chatbot_response(data.message, history)
	return {"received": data.message,
			"response": "Oh no! I am not connected to the chatbot yet!"}


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

	# upload to s3 and textract
	# { "name": filename, "text": "TEXT RESULTS " }
	results = await upload_and_extract(files)

	# The weights:
	weights = user_input['weights']
	del user_input['weights']

	# The premiums:
	async def process_plan(plan_name, plan_content, ):
		ranking_instance = WeightedPlanRanking(weights, plan_content,
											   user_input)
		unweighted_scores = await ranking_instance.ranking_logics()
		weighted_scores = ranking_instance.pair_keys()
		total_score = ranking_instance.total_scores()
		return plan_name, unweighted_scores, weighted_scores, total_score, plan_content

	tasks = [process_plan(name, content) for name, content in results.items()]

	# Run all tasks concurrently
	results = await asyncio.gather(*tasks)

	# Store the results in the history
	for name, unweighted_scores, weighted_scores, total_score, plan_content in results:
		history[name] = {
			"weighted_scores": weighted_scores,
			"total_score": total_score,
			"text": plan_content
		}

		to_frontend[name] = {
			"weightedScores": unweighted_scores,
			"totalScore": total_score,
		}

	return to_frontend

@app.get("/results")
async def get_results():
	return to_frontend
