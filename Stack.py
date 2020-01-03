import Effect
class Stack():
	def __init__(self):
		self.list = [] #list of effects
		self.skip = False
		self.draw = False
		self.drawAmount = 0
		self.reverse_order = False
		self.skipAmount = 0

	def reset(self, draw = False):
		self.list = [] #list of effects
		self.skip = False
		self.skipAmount = 0
		if draw:
			self.draw = False
			self.drawAmount = 0
		self.reverse_order = False

	def add_effect(self, effect):
		self.list.append(effect)

	def execute(self):
		self.reverse_order = bool(len(list(filter(lambda x: x.type == Effect.REVERSE, self.list)))%2)
		self.skipAmount = len(list(filter(lambda x: x.type == Effect.SKIP, self.list)))
		if self.skipAmount > 0:
			self.skip = True
		for x in list(filter((lambda x: x.type == Effect.DRAW), self.list)):
			self.drawAmount += x.amount
		if self.drawAmount > 0:
			self.draw = True

	def isSkip(self):
		return self.skip
	def isDraw(self):
		return self.draw
