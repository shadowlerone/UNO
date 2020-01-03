import Effect
class Card(object):
	def __init__(self, suit, number, effect=Effect.Effect()):
		self.suit = suit
		self.number = number
		self.effect = effect

	def play(self):
		pass

	def __str__(self):
		# print(f"{self.suit} {self.number} ({self.effect})")
		return f"{self.suit} {self.number} ({self.effect})"
