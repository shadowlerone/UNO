DRAW = "draw"
SKIP = "skip"
REVERSE = "reverse"
NONE = "none"
WILD = "wild"
WILDDRAW = "wilddraw"

class Effect(object):
	def __init__(self, effect_type=NONE, amount=NONE, color = NONE, bypass_suit=False):
		self.bypass_suit = bypass_suit
		self.type = effect_type
		if self.isDraw():
			self.amount = amount
		if self.isWild():
			self.color = color

	def isWild(self):
		return (self.type == WILD or self.type == WILDDRAW)
	def isDraw(self):
		return (self.type == DRAW or self.type == WILDDRAW)
	def set_suit(self, suit):
		if self.isWild():
			self.color = suit
	def __str__(self):
		out = f"{self.type}"
		if self.type == DRAW or self.type == WILDDRAW:
			out += f" {self.amount}"
		if self.bypass_suit:
			out += " suitless"
		return out