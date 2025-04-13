from google import genai
from google.genai import types
import os
import dotenv
import asyncio

dotenv.load_dotenv()


class PlanSummaries:
    def __init__(self, plan_content: str, user_age: int, user_budget: float,
                 individual_bool: bool):
        self.plan_content = plan_content
        self.user_age = user_age
        self.user_budget = user_budget
        self.individual = individual_bool

        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(
            api_key=api_key,
        )
        self.model = "gemini-2.0-flash"

    async def get_short_summary(self) -> str:
        response = await self.client.aio.models.generate_content(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=
                f"Summarize the following healthcare insurance plan for a {self.user_age} year old with a budget of {self.user_budget}. Note that if the given boolean is true,"
                f"we are evaluating the plan based on individual coverage. If it is false, we are evaluating the plan based on family coverage. This is given here: {self.individual}"
                f"Given the plan content here. Talk professionally, as though you are an HR representative briefly summarizing the "
                f"plan for an employee. Note the key plan aspects in just 2-3 sentences. Consider the co-payments that are listed for each benefit, and"
                f"be sure to explain any abnormalities. Note the benefits that are expected to be covered, but are not. Note that this is not an interactive chat, thus"
                f"maintain that your responses are not open ended. Do not note reception of this message. Always end with the sentence: '"
                f"If you have more questions, or require a longer summary, please consult with the included chatbot. Here is the plan to summarize.",
                temperature=0.5,
                max_output_tokens=1000,
                top_p=0.8,
                top_k=40
            ),
            contents=self.plan_content
        )
        return response.text
