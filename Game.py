import random
import Card
import Effect
import Deck
import Player
import Stack
import Pile

# constant
UNO = "uno"
LASTCARD = "lastcard"

class Game(object):
	def __init__(self, deck_type = UNO, number_of_players=2):
		self.players = []
		for x in ["test", "myuu"]:
			# name = input(f"Player {x+1}'s name: ")
			self.players.append(Player.Player(x))
		self.deck = Deck.Deck()
		self.pile = Pile.Pile()
		self.stack = Stack.Stack()
		self.player_order = self.players
		self.current_player_number = 0
		self.done = False
		self.draw_check = False
		print(f"Setup finished!")
		for p in self.players:
			p.draw(deck, 7)
		pile.add_card(deck.draw())

	def turn(self):
		self.player_increment = 1
		self.collapse_stack()
		self.current_player_number = (self.current_player_number + self.player_increment) % len(self.player_order)
		turn_player = self.player_order[self.current_player_number]
		print(f"Player {self.player_order[0]}'s turn.")
		print(f"Your Hand: {turn_player.display_hand()}")
		""" if self.draw_check:
			if turn_player.has_effect("draw"):
				drawinput(f"[O: Draw {self.stack.drawAmount}] [1: Play Card With DRAW]")
			else:
				print(f"Drawing {self.stack.drawAmount}")
				for x in range(self.stack.drawAmount):
					turn_player.draw_card(self.deck)
		else:
			pass
		option_string = ", ".join(turn_player.get_playable()) """

		options = turn_player.get_playable(pile.get_playable())
		option_string = "Pick a card: "
		for index, card in enumerate(options):
			option_string += f"[{index}: {card}]"
		choice = input(option_string)
		turn_player.play_card(choice)

		if check_victory(turn_player):
			self.end(turn_player)


	def end(self, player):
		print(f"Congratulations {player}, you won!")
		self.done = True

	def check_victory(self, player):
		if len(player.hand) == 0:
			return True
		else:
			return False

	def check_play(self):
		pass
	def shuffle_deck(self):
		self.deck.shuffle()

	def collapse_stack(self):
		self.stack.execute()
		if self.stack.reverse_order == True:
			self.player_order.reverse()
		elif self.stack.isSkip() == True:
			self.player_increment += self.stack.skipAmount
		if self.stack.isDraw() == False:
			self.stack.reset()
		else:
			self.draw_check = True


if __name__ == "__main__":
	game = Game()
	while not game.done:
		game.turn()


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
