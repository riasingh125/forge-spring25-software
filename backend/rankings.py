from GeminiScript2 import UnweightedPlanRankings


# ===========================
# Weighted Ranking Logic for a plan
class WeightedPlanRanking:
	# Constructs ranking logic object given a set of weights and a corpus
	def __init__(self, weights: dict, corpus: str, user_input: dict):
		self.weights = weights
		self.corpus = corpus
		self.user_input = user_input

		self.scores = dict.fromkeys(self.weights.keys())
		self.weighted_scores = dict.fromkeys(self.weights.keys())
		self.total_score = 0
		self.assign_ranks = UnweightedPlanRankings(self.scores, self.corpus)

	def ranking_logics(self):
		# Implement that stuff here
		self.assign_ranks.assign_benefit_rankings()
		self.assign_ranks.assign_cost_rankings(
			self.user_input['premium'], self.user_input['budget'])
		self.assign_ranks.assign_plan_viability_in_emergency()
		self.assign_ranks.assign_personalized_rankings(
			self.user_input['health_concerns'])
		self.assign_ranks.assign_plan_flexibility(self.user_input['age'])
		self.assign_ranks.assign_convenience_rankings(
			self.user_input['zip_code'], self.user_input['city'],
			self.user_input['state'], self.user_input['health_concerns'])
		self.assign_ranks.assign_geographic_rankings()

		self.scores = self.assign_ranks.get_rankings()

	# Assigns each category a weighted score
	def pair_keys(self):
		for i in self.weights.keys():
			self.weighted_scores[i] = self.weights[i] * self.scores[i]

	# Returns the total score for this corpus
	def total_scores(self):
		self.total_score = sum(self.weighted_scores.values())
		return self.total_score
