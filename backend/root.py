from fastapi import FastAPI, File, UploadFile
from typing import List
from models import UserInputForm
from models import ChatBotMessage

# import function to upload files to s3
from upload_extract import upload_and_extract

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

@app.post("/chat/message")
async def send_message(data: ChatBotMessage):
    return {"received": data.message, "response": "hi"}

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

@app.post("/form/upload-pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):

    for file in files:
        if file.content_type != 'application/pdf':
            return {"error" : "file is not of type pdf"}

    results = await upload_and_extract(files)
    for result in results:
        print(result)

    return {"message" : "successfully uploaded files", "textract": results}


@app.get("/results")
async def get_results():
    return {
        "results": [
            {"name": "Plan A", "price": "$100"},
            {"name": "Plan B", "price": "$200"},
            {"name": "Plan C", "price": "$300"}
        ]
    }