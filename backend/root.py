from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from models import UserInputForm
from models import ChatBotMessage
import json

# import function to upload files to s3
from upload_extract import upload_and_extract

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow frontend in React to conncet
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

@app.post("/chat/message")
async def send_message(data: ChatBotMessage):
    return {"received": data.message, "response": "hi"}


@app.post("/form/submit")
async def upload_pdfs(form_data:str = Form(...), files: List[UploadFile] = File(...)):

    # Process form data into dictionary
    form_dict = json.loads(form_data)

    # Check against Pydantic Model
    #user_input = UserInputForm(**form_dict)

    # check files for right type:
    for file in files:
        if file.content_type != 'application/pdf':
            return {"error" : "file is not of type pdf"}

    # upload to s3 and textract
    results = await upload_and_extract(files)

    return {"userInput" : form_dict, "textract": results}


@app.get("/results")
async def get_results():
    return {
        "results": [
            {"name": "Plan A", "price": "$100"},
            {"name": "Plan B", "price": "$200"},
            {"name": "Plan C", "price": "$300"}
        ]
    }