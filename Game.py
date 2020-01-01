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


class Stack():
	def __init__(self):
		self.list = [] #list of effects
		self.skip = False
		self.draw = False
		self.drawAmount = 0
		self.reverse_order = False

	def reset(self):
		self.list = [] #list of effects
		self.skip = False
		self.draw = False
		self.drawAmount = 0
		self.reverse_order = False

	def add_effect(self, effect):
		self.list += effect

	def execute(self):
		self.reverse_order = bool(len(list(filter(lambda x: x.type == effect, self.list)))%2)

	def isSkip(self):
		return self.skip
	def isDraw(self):
		return self.draw



class Effect(object):
	def __init__(self, effect_type=None, amount=None, bypass_suit=False):
		self.bypass_suit = bypass_suit
		self.type = effect_type
		if self.type == "draw":
			self.amount = amount
		else:
			self.amount = None




class Card(object):
	def __init__(self, suit, number, effect=Effect(False)):
		self.suit = suit
		self.number = number
		self.effect = effect

	def play(self):
		pass

	def __str__(self):
		return f"{self.suit} {self.number}"


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


class Deck(object):
	def __init__(self, type=UNO):
		self.list = deck_format(type)

	def draw(self):
		return self.list.pop()

	def shuffle(self):
		random.shuffle(self.list)


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
