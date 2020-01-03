
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.playable = []

	def draw_card(self, deck, amount = 1):
		for x in range(amount):
			self.hand.append(deck.draw())

	def play_card(self, index):
		self.hand.remove(self.playable[index])
		return self.playable.pop(index)

	def get_playable(self, suit=None, number=None):
		self.playable = list(filter(lambda x: (x.suit == suit or x.effect.bypass_suit == True) or x.number == number, self.hand))
		return self.playable

	def __str__(self):
		return self.name
	def display_hand(self):
		out = ""
		for index, card in enumerate(self.hand):
			out += f"[{index}: {card}] "
		return out

	def has_suit(self, suit):
		return len(list(filter(lambda x: x.suit == suit, turn_player.hand))) > 0
	def has_number(self, suit):
		return len(list(filter(lambda x: x.number == number, turn_player.hand))) > 0
	def has_effect(self, effect):
		return len(list(filter(lambda x: x.effect.type == effect, self.hand))) > 0

