from fastapi import FastAPI, status
from pydantic import BaseModel

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


# ===========================
# User Form Input / Results
# ===========================

# Format for user form input
class UserInputForm(BaseModel):
    insurance_id: int
    age: int
    income: float
    email: str
    number: int
    city : str
    state: str
    zip_code: int
    number_of_people_needing_coverage: int
    ages_of_people_needing_coverage: list[int]
    budget: float
    personal_health_concerns: str
    # Weights for the data
    age_weight: int
    income_weight: int
    city_weight: int
    zip_code_weight: int
    number_of_people_needing_coverage_weight: int
    ages_of_people_needing_coverage_weight: int
    budget_weight: int
    personal_health_concerns_weight: int

    class Config:
        extra = "allow"

# Endpoint for sending user input from form
# 'data' parameters corresponds to JSON body in POST request
@app.post("/form/send")
async def send_form(data: UserInputForm):
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

# ===========================
# Ranking Logic for the program.
class RankingLogic:
    # Constructs ranking logic object given a set of weights and a corpus
    def __init__(self, weights: dict, corpus):
        self.weights =  weights
        self.corpus = corpus

        self.scores = dict.fromkeys(self.weights.keys())
        self.weighted_scores = dict.fromkeys(self.weights.keys())
        self.total_score = 0


    #TODO: Implement the ranking logic, connect to AWS. Currently placeholder
    def ranking_logics(self):
        #Implement that stuff here
        for key, value in self.weights.items():
            self.scores[key] = 0
            print(self.scores)

    # Assigns each category a weighted score
    def pair_keys(self):
        for i in self.weights.keys():
            self.weighted_scores[i] = self.weights[i] * self.scores[i]

    # Returns the total score for this corpus
    def total_scores(self):
        self.total_score = sum(self.weighted_scores.values())
        return self.total_score
