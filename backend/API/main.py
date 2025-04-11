from backend.RankingLogics import rankings
import asyncio


def main():
	plan = rankings.WeightedPlanRanking(
		weights={
			'coverage_of_all_benefits': 0.0,
			'affordability': 1,
			'personalized_coverage': 0.0,
			'emergency_coverage': 0.0,
			'flexibility_of_coverage': 0.1,
			'convenience_of_coverage': 0.0,
			'geographic_coverage': 0.0
		},
		corpus='',
		user_input={
			"premium": 100,
			"budget": 200,
			"health_concerns": "Diabetes",
			"age": 30,
			"zip_code": "14127",
			"city": "OP",
			"state": "New York"
		}
	)

	asyncio.run(plan.ranking_logics())
	print(plan.scores)
	print(plan.pair_keys())
	print(plan.total_scores())
	print(plan.weighted_scores)


main()
