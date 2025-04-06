import asyncio

from GeminiScript2 import UnweightedPlanRankings
from Budget import Budget


# ===========================
# Weighted Ranking Logic for a plan
class WeightedPlanRanking:
	# Constructs ranking logic object given a set of weights and a corpus
	def __init__(self, weights: dict, corpus: str, user_input: dict, premium: float = 150.):
		self.weights = weights
		self.corpus = corpus
		self.user_input = user_input
		self.premium= premium
		self.scores = dict.fromkeys(self.weights.keys())
		self.weighted_scores = dict.fromkeys(self.weights.keys())
		self.total_score = 0
		self.assign_ranks = UnweightedPlanRankings(self.scores, self.corpus)

	async def ranking_logics(self):
		k = self.user_input['budget']
		budget_class = Budget.classify_budget(k)
		# Implement that stuff here
		await asyncio.gather(
			self.assign_ranks.assign_benefit_rankings(),
			self.assign_ranks.assign_cost_rankings(
				self.premium, budget_class),
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
			self.weighted_scores[i] = self.weights[i] * self.scores[i]
		return self.weighted_scores

	# Returns the total score for this corpus
	def total_scores(self):
		optimal_score = sum([i * 10 for i in self.weights.values()])
		self.total_score = sum(self.weighted_scores.values()) / optimal_score
		return self.total_score
