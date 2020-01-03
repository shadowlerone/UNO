class Pile(object):
	def __init__(self):
		self.list = []
		self.suit_override = None

	def check_play(self, card):
		out = False
		if card.effect.bypass_suit:
			out = True
		elif card.suit == self.list[-1].suit:
			out = True
		elif card.number == self.list[-1].number:
			out = True
		return out
	def add_card(self, card):
		self.list.append(card)
		self.suit_override = None

	def get_playable(self):
		if self.suit_override != None:
			return self.suit_override, self.list[-1].number
		else:
			return self.list[-1].suit, self.list[-1].number

	def top(self):
		return self.list[-1]