from Observable import Observable

class GarbageBin(Observable):

	def __init__(self):
		self.contents = [] 
		self.MAX_SIZE = 4
		self.possible_states = ["FULL","STINKY","HALF_FULL","TO_BE_WASHED"]

	def TakeOutTrash(self):
		self.contents = None

	def PutTrashIn(self,trash):
		if len(self.contents) < self.MAX_SIZE:
			self.contents.append(trash)
			notify(self.possible_states[2])
			if trash == "ROTTEN_TOMATOES":
				notify(self.possible_states[1])
		else:
			notify(self.possible_states[0])			
