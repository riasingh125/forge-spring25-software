from google import genai
from google.genai import types
import os
import dotenv
import asyncio

dotenv.load_dotenv()


class PlanSummaries:
	def __init__(self, plan_content: str, user_age: int, user_budget: float):
		self.plan_content = plan_content
		self.user_age = user_age
		self.user_budget = user_budget

		api_key = os.getenv("GEMINI_API_KEY")
		self.client = genai.Client(
			api_key=api_key,
		)
		self.model = "gemini-2.0-flash"

	async def get_plan_summary(self) -> str:
		response = await self.client.aio.models.generate_content(
			model=self.model,
			contents=[
				f"Summarize the following healthcare insurance plan for a {self.user_age} year old with a budget of {self.user_budget}."
				f"Given is the plan content here. Talk professionally, as though you are an HR representative briefly summarizing the "
				f"plan for an employee. Try to note the key points in 2-3 sentences. Note that this is not an interactive chat, thus"
				f"maintain that your responses are not open ended.\n\n{self.plan_content}"
			],
			config=genai.types.GenerateContentConfig(
				temperature=0.5,
				max_output_tokens=1000,
				top_p=0.8,
				top_k=40,
			),
		)
		return response.text

	async def get_all_plan_summaries(self, previous_message:str) -> str:
		response = await self.client.aio.models.generate_content(
			model = self.model,
			contents = [
				f"Summarize the following healthcare insurance plan for a {self.user_age} year old with a budget of {self.user_budget}."
				f"Given is the plan content here. Talk professionally, as though you are an HR representative briefly summarizing the "
				f"plan for an employee. Note that there was a previous chat, and your response should be in the context of that chat. Put "
				f"simply, you should directly incorporate the previous message as the first sentences of your response. From there, give another 3-4 sentences"
				f"that go into more detail about the plan. Here is that plan: {previous_message}. Note that this is not an interactive chat, thus maintain that your responses"
				f"are not open ended.\n\n{self.plan_content}"
			],
			config = genai.types.GenerateContentConfig(
				temperature = 0.5,
				max_output_tokens = 1000,
				top_p = 0.8,
				top_k = 40,
			),
		)
