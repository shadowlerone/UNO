import Effect
class Card(object):
	def __init__(self, suit, number, effect=Effect.Effect()):
		self.suit = suit
		self.number = number
		self.effect = effect
	def __str__(self):
		return f"{self.suit} {self.number} ({self.effect})"
