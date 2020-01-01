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

class Deck(object):
	def __init__(self, type=UNO):
		self.list = deck_format(type)

	def draw(self):
		return self.list.pop()

	def shuffle(self):
		random.shuffle(self.list)