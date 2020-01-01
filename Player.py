
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.playable = []

	def draw_card(self, deck):
		self.hand += deck.draw()

	def play_card(self, index):
		return self.playable.pop(index)

	def get_playable(self, suit=None, number=None, effect=None):
		self.playable = list(filter(lambda x: x.suit == suit or x.number == number or x.effect.type == effect, turn_player.hand))
		return list(filter(lambda x: x.suit == suit or x.number == number or x.effect.type == effect, turn_player.hand))

	def __str__(self):
		return self.name
	def display_hand(self):
		return ",".join(self.hand)
	def has_suit(self, suit):
		return len(list(filter(lambda x: x.suit == suit, turn_player.hand))) > 0
	def has_number(self, suit):
		return len(list(filter(lambda x: x.number == number, turn_player.hand))) > 0
	def has_effect(self, effect):
		return len(list(filter(lambda x: x.effect.type == effect, self.hand))) > 0
