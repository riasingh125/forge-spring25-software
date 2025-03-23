from pyexpat.errors import messages

from fastapi import FastAPI, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel


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



# Sending Message
@app.post("/chat/message")
async def send_message(data: ChatBotMessage):
    return {"received": data.message, "response": "hi"}


# Sending Form
@app.post("/form/send")
async def send_form(data: UserInputForm):
    return {"total_score": 100}



@app.get("/results")
async def get_results():
    return {
        "results": [
            {"name": "Plan A", "price": "$100"},
            {"name": "Plan B", "price": "$200"},
            {"name": "Plan C", "price": "$300"}
        ]
    }





sections = ["coverage", "contact", "address", "weights"]
# Gets missing fields from request error
def clean_errors(errors):
    data = {}
    for error in errors:
        loc = error["loc"]
        if error["type"] == "missing":
            if not "missing" in loc:
                data["missing"] = []
            field = error["loc"][1]
            if len(error["loc"]) == 3:
                field += ": " + error["loc"][2]
            elif field in sections:
                field = "Section: "+field
            data["missing"].append(field)
        else:
            if not "invalid" in data:
                data["invalid"] = []
            data["invalid"].append({loc[-1] : error["msg"]})

    return data

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    modified_response = {
        "error": "Your request body is not formatted correctly.",
        "errors": clean_errors(exc.errors()),
        "original_error" : exc.errors()
    }
    return JSONResponse(
        status_code=422,
        content=modified_response
    )




