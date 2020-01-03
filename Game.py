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
		for x in range(number_of_players):
			name = input(f"Player {x+1}'s name: ")
			self.players.append(Player.Player(name))
		self.deck = Deck.Deck()
		self.shuffle_deck()
		self.pile = Pile.Pile()
		self.stack = Stack.Stack()
		self.player_order = self.players
		self.current_player_number = 0
		self.done = False
		self.draw_check = False
		print(f"Setup finished!")
		for p in self.players:
			p.draw_card(self.deck, 7)
		self.pile.add_card(self.deck.draw())

	def turn(self):
		self.player_increment = 1
		self.collapse_stack()
		self.current_player_number = (self.current_player_number + self.player_increment) % len(self.player_order)
		turn_player = self.player_order[self.current_player_number]
		print(f"Player {turn_player}'s turn.")
		print(f"Your Hand: {turn_player.display_hand()}")
		if self.draw_check:
			if turn_player.has_effect("draw"):
				drawinput(f"[O: Draw {self.stack.drawAmount}] [1: Play Card With DRAW]")
			else:
				print(f"Drawing {self.stack.drawAmount}")
				for x in range(self.stack.drawAmount):
					turn_player.draw_card(self.deck)
		else:
			pass
		option_string = ", ".join(turn_player.get_playable())
		print(f"Top of Pile: {self.pile.top()}")
		options = turn_player.get_playable(self.pile.top().suit, self.pile.top().number)
		if len(options) == 0:
			input("You cannot play anything. Press Enter to draw a card.\n>")
			turn_player.draw_card(self.deck)
			options = turn_player.get_playable(self.pile.top().suit, self.pile.top().number)
			if len(options) == 0:
				input(f"The card you drew ({turn_player.hand[-1]}) could not be played.\n>")
				return
		option_string =""
		for index, card in enumerate(options):
			option_string += f"[{index}: {card}]"
		choice = int(input(f"Pick a card: {option_string}\n>"))
		self.pile.add_card(turn_player.play_card(choice))

		if self.check_victory(turn_player):
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
