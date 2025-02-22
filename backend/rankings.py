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
