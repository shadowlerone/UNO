DRAW = "draw"
SKIP = "skip"
REVERSE = "reverse"
NONE = "none"

class Effect(object):
	def __init__(self, effect_type=NONE, amount=NONE, bypass_suit=False):
		self.bypass_suit = bypass_suit
		self.type = effect_type
		if self.type == DRAW:
			self.amount = amount
		else:
			self.amount = None

	def __str__(self):
		out = f"{self.type}"
		if self.type == DRAW:
			out += f" {self.amount}"
		if self.bypass_suit:
			out += " suitless"
		return out