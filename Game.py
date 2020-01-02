import random
import Card
import Effect
import Deck
import Player
import Stack

# constant
UNO = "uno"
LASTCARD = "lastcard"

class Game(object):
	def __init__(self, deck_type = UNO, number_of_players=2):
		self.players = []
		for x in range(number_of_players):
			name = input(f"Player {x+1}'s name: ")
			self.players += Player.Player(name)
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
			self.player_increment += self.stack.skipAmount
		if self.stack.isDraw() == False:
			self.stack.reset()
		else:
			self.draw_check = True


if __name__ == "__main__":
	#deck test
	deck = Deck.Deck()
	print(deck.list)
	#Stack + effect test
	stack = Stack.Stack()
	skip_effect = Effect.Effect(Effect.SKIP)
	draw_two_effect = Effect.Effect(Effect.DRAW, amount = 2)
	draw_four_effect = Effect.Effect(Effect.DRAW, amount = 4)
	stack.add_effect(skip_effect)
	stack.add_effect(draw_four_effect)
	stack.add_effect(draw_two_effect)
	stack.add_effect(Effect.Effect(Effect.REVERSE))
	stack.add_effect(Effect.Effect(Effect.REVERSE))
	stack.execute()
	print(f"Draw? {stack.isDraw()}")
	print(f"Skip? {stack.isSkip()}")
	print(f"Draw amount: {stack.drawAmount}")
	print(f"Skip Amount {stack.skipAmount}")
	deck.shuffle()
	test_player = Player.Player("Test")
	print(f"Deck length: {len(deck.list)}")
	print(f"Deck Last Card: {deck.list[-1]}")
	print(f"Player hand length: {len(test_player.hand)}")
	test_player.draw_card(deck)
	print(f"Deck length: {len(deck.list)}")
	print(f"Deck Last Card: {deck.list[-1]}")
	print(f"Player hand length: {len(test_player.hand)}")
	print(f"Player Hand: {test_player.display_hand()}")


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
