DRAW = "draw"
SKIP = "skip"

class Effect(object):
	def __init__(self, effect_type=None, amount=None, bypass_suit=False):
		self.bypass_suit = bypass_suit
		self.type = effect_type
		if self.type == "draw":
			self.amount = amount
		else:
			self.amount = None