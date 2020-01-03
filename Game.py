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
		""" self.players.append(Player.Player("Shadow"))
		self.players.append(Player.Player("Lerone"))
		self.players.append(Player.Player("Steicy")) """
		self.deck = Deck.Deck()
		self.shuffle_deck()
		self.pile = Pile.Pile()
		self.stack = Stack.Stack()
		self.player_order = self.players
		self.current_player_number = 0
		self.done = False
		self.draw_check = False
		self.last_player_number = 0
		print(f"Setup finished!")
		for p in self.players:
			p.draw_card(self.deck, 7)
		self.pile.add_card(self.deck.draw())

	def turn(self):
		self.player_increment = 1
		self.collapse_stack()
		self.current_player_number = (self.last_player_number + self.player_increment) % len(self.player_order)
		turn_player = self.player_order[self.current_player_number]
		print(f"Player {turn_player}'s turn.")
		print(f"Your Hand: {turn_player.display_hand()}")
		self.last_player_number = self.current_player_number
		playable_suit, playable_number = self.pile.get_playable()

		if self.draw_check:
			if len(turn_player.get_playable(playable_suit, effect = Effect.DRAW, strict = True)) > 0:
				draw = bool(self.get_input(f"[O: Draw {self.stack.drawAmount}] [1: Play Card With DRAW]\n>", min = 0, max = 1))
				if draw:
					options = turn_player.get_playable(playable_suit, effect = Effect.DRAW, strict = True)
				else:
					input(f"Drawing {self.stack.drawAmount} cards.\n>")
					turn_player.draw_card(self.deck, self.stack.drawAmount)
					self.stack.reset(True)
					return
			else:
				input(f"Drawing {self.stack.drawAmount} cards.\n>")
				turn_player.draw_card(self.deck, self.stack.drawAmount)
				self.stack.reset(draw = True)
				return
		else:
			options = turn_player.get_playable(playable_suit, playable_number)
		print(f"Top of Pile: {self.pile.top()}")
		if len(options) == 0:
			input("You cannot play anything. Press Enter to draw a card.\n>")
			turn_player.draw_card(self.deck)
			options = turn_player.get_playable(self.pile.top().suit, self.pile.top().number)
			if len(options) == 0:
				input(f"The card you drew ({turn_player.hand[-1]}) could not be played.\n>")
				return
		option_string = self.input_format(options)
		choice = self.get_input(f"Pick a card: {option_string}\n>", min = 0, max = len(options) -1)
		played = turn_player.play_card(choice)
		if played.effect.isWild():
			suits_selection = self.input_format(self.deck.suits)
			suit = self.get_input(f"Select suit: {suits_selection}:\n>")
			played.effect.color = self.deck.suits[suit]
		self.pile.add_card(played)
		self.stack.add_effect(played.effect)

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
		if self.stack.suit_override != None:
			self.pile.suit_override = self.stack.suit_override
		if self.stack.reverse_order == True:
			self.player_order.reverse()
			self.last_player_number = (self.last_player_number + len(self.players) - 1) % len(self.players)
		if self.stack.skip:
			self.player_increment += self.stack.skipAmount
		if self.stack.isDraw() == False:
			self.draw_check = False
			self.stack.reset()
		else:
			self.draw_check = True

	def input_format(self, options):
		out = ""
		for index, option in enumerate(options):
			out += f"[{index}: {option}]"
		return out

	def get_input(self, string, min = 0, max = None):
		can_out = False
		while not can_out:
			try:
				out = int(input(string))
				if out < max and out > min:
					can_out = True
			except:
				print("Your input is invalid")


if __name__ == "__main__":
	game = Game()
	while not game.done:
		game.turn()
