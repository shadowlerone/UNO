import Effect
class Card(object):
	def __init__(self, suit, number, effect=Effect.Effect(False)):
		self.suit = suit
		self.number = number
		self.effect = effect

	def play(self):
		pass

	def __str__(self):
		return f"{self.suit} {self.number}"
