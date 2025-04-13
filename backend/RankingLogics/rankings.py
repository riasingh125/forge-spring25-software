import asyncio

from .UnweightedPlanRankings import UnweightedPlanRankings
from .Budget import Budget
import copy

# ===========================
# Weighted Ranking Logic for a plan
class WeightedPlanRanking:
	# Constructs ranking logic object given a set of weights and a corpus
	def __init__(self, weights: dict, corpus: str, user_input: dict, premium: float, individual_bool: bool):
		self.weights = weights
		self.corpus = corpus
		self.user_input = user_input
		self.premium= premium
		self.individual = individual_bool
		self.scores = dict.fromkeys(self.weights.keys())
		self.weighted_scores = dict.fromkeys(self.weights.keys())
		self.total_score = 0
		self.assign_ranks = UnweightedPlanRankings(self.scores, self.corpus)

	async def ranking_logics(self):
		k = self.user_input['budget']
		budget_class = Budget.classify_budget(k)
		# Implement that stuff here
		await asyncio.gather(
			self.assign_ranks.assign_benefit_rankings(self.individual),
			self.assign_ranks.assign_cost_rankings(
				self.premium, budget_class, self.individual),
			self.assign_ranks.assign_plan_viability_in_emergency(),
			self.assign_ranks.assign_personalized_rankings(
				self.user_input['health_concerns']),
			self.assign_ranks.assign_plan_flexibility(self.user_input['age']),
			self.assign_ranks.assign_convenience_rankings(
				self.user_input['zip_code'], self.user_input['city'],
				self.user_input['state'], self.user_input['health_concerns']),
			self.assign_ranks.assign_geographic_rankings())

		self.scores = self.assign_ranks.get_rankings()
		return self.scores


	# Assigns each category a weighted score
	def pair_keys(self):
		for i in self.weights.keys():
			self.weighted_scores[i] = round(self.weights[i] * self.scores[i],2)
		return self.weighted_scores

	# Returns the total score for this corpus
	def total_scores(self):
		optimal_score = sum([i * 10 for i in copy.deepcopy(self.weights).values()])
		self.total_score = round(sum(copy.deepcopy(self.weighted_scores).values()) / optimal_score * 10, 2)
		return self.total_score
