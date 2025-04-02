import base64
import os
from google import genai
from google.genai import types

from backend.Budget import Budget


class AssignRankings:
	def __init__(self, rankings: dict, user_plan: str):
		self.client = genai.Client(
			api_key="",
		)
		self.model = "gemini-2.5-pro-exp-03-25"
		self.rankings = rankings
		self.plan = user_plan

	def assign_benefit_rankings(self):
		response = self.client.models.generate_content(
			model=self.model,
			config=types.GenerateContentConfig(
				system_instruction="Evaluate the provided healthcare insurance plan as an expert and assign a score based on both state and nationwide benchmarks."
								   "# Instructions- Review the healthcare insurance plan details."
								   "- Evaluate the plan's benefits and costs relative to current state and nationwide insurance benchmarks."
								   "- Note that there is no reason to artificially inflate or deflate the score, as accuracy is critical."
								   "- Assign a score from 1 to 10, with 1 being the lowest and 10 the highest, based on this evaluation."
								   "# Output Format\- Provide a score between 1 and 10.- "
								   "Simply output a number for the given benefit, referencing the specific benchmarks considered. Be careful to not output "
								   "reasoning or ANY other information than the number. Wait for the "
								   "next instruction before proceeding.",
				temperature=0

			),
			contents=self.plan
		)
		self.rankings["benefit_score"] = int(response.text)
		return None

	def assign_cost_rankings(self, cost: float, budget: Budget):
		response = self.client.models.generate_content(
			model=self.model,
			config=types.GenerateContentConfig(
				system_instruction=f"Compared to the monthly premium of ${cost} per month, evaluate the cost of the healthcare insurance plan."
								   f"The object of this is to not evaluate the benefits, but the cost of the plan in the wider context of the plan premium."
								   f"Thus, this plan should be compared to what plans with these benefit costs would typically cost for their premium. "
								   f"Note that there is no reason to artificially inflate or deflate the score, as accuracy is critical."
								   f"Assign a score from 1 to 10, with 1 being the lowest and 10 the highest, based on this evaluation."
								   f"# Output Format\- Provide a score between 1 and 10.- "
								   f"Simply output a number for the given benefit, referencing the specific benchmarks considered. Be careful to not output "
								   f"reasoning or ANY other information than the number. Wait for the "
								   f"next instruction before proceeding.",
				temperature=0
			),
			contents=self.plan
		)
		self.rankings['cost_score'] = int(response.text)
		return None

	def assign_personalized_rankings(self, user_input: str):
		response = self.client.models.generate_content(
			model=self.model,
			config=types.GenerateContentConfig(
				system_instruction=f"You are an expert advisor in healthcare insurance evaluation. Based on the user's "
								   f"personal health concerns, evaluate the insurance plan objectively and assign a score "
								   f"from 1 to 10, where 1 represents a poor plan and 10 represents an excellent plan. "
								   f"Consider that the cost for specific treatments may be high or the plan may not cover certain "
								   f"conditions. Use national benchmarks and typical coverage costs for the ailments mentioned in the user input. "
								   f"Output ONLY the numerical score"
								   f"Do not include any extra reasoning, explanation, or commentary. "
								   f"After providing the score, wait for further instructions. "
								   f"User input: {user_input}",
				temperature=0
			),
			contents=self.plan
		)
		self.rankings['personalized_score'] = int(response.text)
		return None

	def assign_plan_flexibility(self, age: int):
		response = self.client.models.generate_content(
			model=self.model,
			config=types.GenerateContentConfig(
				system_instruction=f"Evaluate the healthcare insurance plan's flexibility in terms of coverage for "
								   f"individuals aged {age}. Note the most common diseases and injuries for the individual's age group"
								   f"by researching national statistics, but be sure to not overstate one's likelihood to gather one of these diseases."
								   f" Consider the plan's coverage for these conditions and how well it meets the needs of individuals in this age group."
								   f" Be especially considerate of the percentage of individuals in this age group who are likely to be affected by these conditions, "
								   f"as to not  understate this plan's score."
								   f" Assign a score from 1 to 10, where 1 indicates poor flexibility and "
								   f"10 indicates excellent flexibility. Provide only the numerical score, without any additional "
								   f"reasoning or commentary. Wait for further instructions after providing the score.",
				temperature=0
			),
			contents=self.plan
		)
		self.rankings['flexibility_score'] = int(response.text)
		return None

	def assign_convenience_rankings(self, zip_code: int, city: str, state: str,
									user_input: str):
		response = self.client.models.generate_content(
			model=self.model,
			config=types.GenerateContentConfig(
				system_instruction=f"Evaluate the healthcare insurance plan's convenience to access coverage based on the provided zip code {zip_code}, city {city}, and state {state}. "
								   f" Consider the availability of healthcare providers, hospitals, and specialists in the area. Consider the ailments mentioned in the user input, given as this: {user_input}. "
								   f" Consider how easy it would be to access coverage for these ailments in this area. Do not take into account the cost of accessing the benefit, or cost at all. Solely "
								   f"consider the convenience of accessing the coverage. Assume the individual is local, and does not want to be traveling to access the coverage. "
								   f"Assign a score from 1 to 10, where 1 indicates poor convenience and "
								   f"10 indicates excellent convenience. Provide only the numerical score, without any additional "
								   f"reasoning or commentary. Wait for further instructions after providing the score.",
				temperature=0
			),
			contents=self.plan
		)
		self.rankings['convenience_score'] = int(response.text)
		return None

	def assign_geographic_rankings(self):
		response = self.client.models.generate_content(
			model=self.model,
			config=types.GenerateContentConfig(
				system_instruction=f"Evaluate the healthcare insurance plan's geographic coverage. Consider the plan's coverage in terms of the plans coverage, should they happen to be traveling for any reason."
								   f"You should evaluate exactly how well this plan covers the individual in the event they are traveling, and how well it covers them outside of just their home state."
								   f"Assign a score from 1 to 10, where 1 indicates poor geographic coverage and "
								   f"10 indicates excellent geographic coverage. Provide only the numerical score, without any additional "
								   f"reasoning or commentary. Wait for further instructions after providing the score.",
				temperature=0
			),
			contents=self.plan
		)
		self.rankings['geographic_score'] = int(response.text)
		return None

	def get_rankings(self):
		return self.rankings
