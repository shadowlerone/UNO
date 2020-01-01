import random
import Card


# constant
UNO = "uno"
LASTCARD = "lastcard"

def uno_deck():
	template = []
	for x in range(10):
		template += [[x, None] *2]
	return template



def deck_format(type):
	temp = uno_deck()
	# print(temp)
	out = []
	for suit in ["red", "blue", "green", "yellow"]:
		for x in temp:
			out += [Card(suit, x[0], x[1])]
	return out

class Game(object):
	def __init__(self, deck_type = UNO, number_of_players=2):
		self.players = []
		for x in range(number_of_players):
			name = input(f"Player {x+1}'s name: ")
			self.players += Player(name)
		self.deck = Deck()
		self.pile = Pile()
		self.stack = []
		self.player_order = self.players
		self.current_player_number = 0
		self.draw_check = False
		print(f"Setup finished!")

	def turn(self):
		self.player_increment = 1
		self.collapse_stack()
		self.current_player_number = (self.current_player + self.player_increment) % len(self.player_order)
		turn_player = self.player_order[self.current_player_number]
		print(f"Player {self.player_order[0]}'s turn.'")
		added_options = []
		if self.draw_check and not turn_player.has_effect("draw"):
			for x in range(self.stack.drawAmount):
				turn_player.draw_card(self.deck)
		else:
			added_options += []
		option_string = ", ".join(turn_player.get_playable())

	def check_play(self):
		pass
	def shuffle_deck(self):
		self.deck.shuffle()

	def collapse_stack(self):
		self.stack.execute()
		if self.stack.reverse == True:
			self.player_order.reverse()
		elif self.stack.isSkip() == True:
			self.player_increment = 2
		if self.stack.isDraw() == False:
			self.stack.reset()
		else:
			self.draw_check = True

class Effect(object):
	def __init__(self, effect_type=None, amount=None, bypass_suit=False):
		self.bypass_suit = bypass_suit
		self.type = effect_type
		if self.type == "draw":
			self.amount = amount
		else:
			self.amount = None



"""
Process of a game of UNO
Deck is generated
Deck is shuffled

Numbers of players is selected
cards are drawn

Core loop
Turn Start
Select Card to play
activate card effects, if any
check if player hand is 0
	if true, game ends, tht player wins





"""
