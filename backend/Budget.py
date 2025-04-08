from enum import Enum
import math

class Budget(Enum):
	VERY_LOW = (0, 300)
	LOW = (301, 450)
	MEDIUM = (451, 650)
	HIGH = (651, 850)
	VERY_HIGH = (851, math.inf)

	# Class method that returns the enum classification for a given premium.
	@classmethod
	def classify_budget(cls, desired_premium:float):
		if desired_premium < 0:
			raise ValueError("Desired premium cannot be negative.")
		for budget in Budget:
			lower, upper = budget.value
			if lower<= desired_premium <= upper:
				return budget
		return None

