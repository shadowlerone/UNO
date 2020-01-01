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
