class Pile(object):
	def __init__(self):
		self.list = []

	def check_play(self, card):
		out = False
		if card.effect.bypass_suit:
			out = True
		elif card.suit == self.list[-1].suit:
			out = True
		elif card.number == self.list[-1].number:
			out = True
		return out