import base64
import os
from google import genai
from google.genai import types


class AssignRankings:
	def __init__(self, rankings: dict, user_plan: str):
		self.client = genai.Client(
			api_key=os.environ.get("GEMINI_API_KEY"),
		)
		self.model = "gemini-2.5-pro-exp-03-25"
		self.rankings = rankings
		self.plan = user_plan

	def assign_benefit_rankings(self):
		model = self.model
		response = self.client.models.generate_content(
			model=self.model,
			config=types.GenerateContentConfig(
				"Evaluate the provided healthcare insurance plan as an expert and assign a score based on nationwide benchmarks."
				"# Instructions- Review the healthcare insurance plan details."
				"- Evaluate the plan's benefits and costs relative to current nationwide insurance benchmarks."
				"- Assign a score from 1 to 10, with 1 being the lowest and 10 the highest, based on this evaluation."
				"# Output Format\- Provide a score between 1 and 10.- "
				"Simply output a number for the given benefit, referencing the specific benchmarks considered. Wait for the "
				"next instruction before proceeding."),
			contents=self.plan
		)

		self.rankings["benefit_score"] = int(response.text)