from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from PlanSummaries import PlanSummaries
from rankings import WeightedPlanRanking
from models import UserInputForm
from models import ChatBotMessage
import json

# import function to upload files to s3
from upload_extract import upload_and_extract
# import function to get chabot response
from chatbot import get_chatbot_response
import asyncio

content = ""
with open("test.txt", 'r') as file:
	# Read the entire content of the file
	content = file.read()
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


@app.get("/")
def root():
	return {"FastAPI Running!!!!!"}


@app.post("/chat/message")
async def send_message(data: ChatBotMessage):
	response = "Hello World!"
	return {"received": data.message, "response": response}


@app.post("/form/submit")
async def upload_pdfs(form_data: str = Form(...),
					  files: List[UploadFile] = File(...)):
	to_frontend = [{
		"name": "Plan 1",
		"weightedScores": {
			'coverage_of_all_benefits': 1.6,
			'affordability': 2.0,
			'personalized_coverage': 3.5,
			'emergency_coverage': 1.0,
			'flexibility_of_coverage': 2.5,
			'convenience_of_coverage': 6.0,
			'geographic_coverage': 7.5
		},
		"totalScore": 3.5,
		"shortSummary": "This is a short summary of the plan",
	}]

	return to_frontend
