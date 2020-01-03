import Card
import random
import Effect

UNO = "uno"
LASTCARD = "lastcard"

def uno_deck():
	template = []
	for x in range(10):
		template.append(x)
		template.append(x)
	# print(template)
	return template



def deck_format(type):
	temp = uno_deck()
	# print(temp)
	out = []
	for suit in ["red", "blue", "green", "yellow"]:
		for x in temp:
			out.append(Card.Card(suit, x))
	return out

class Deck(object):
	def __init__(self, type=UNO):
		self.list = deck_format(type)

	def draw(self):
		return self.list.pop()

	def shuffle(self):
		random.shuffle(self.list)