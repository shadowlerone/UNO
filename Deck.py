class Deck(object):
	def __init__(self, type=UNO):
		self.list = deck_format(type)

	def draw(self):
		return self.list.pop()

	def shuffle(self):
		random.shuffle(self.list)