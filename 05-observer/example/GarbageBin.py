from Observable import Observable

class GarbageBin(Observable):
	""" Represents a Garbage bin"""
	def __init__(self,size = 4):
		super(GarbageBin,self).__init__()
		self.contents = [] 
		self.MAX_SIZE = size
		self.possible_states = ["FULL","STINKY","HALF_FULL","EMPTY"]

	def take_out_trash(self):
		self.contents = [] 
		print "Trash is emptied"
		self.notify_observers(self.possible_states[3])

	def put_trash_in(self,trash):
		print trash,"was thrown in the bin"
		if len(self.contents) < self.MAX_SIZE:
			self.contents.append(trash)
			self.notify_observers(self.possible_states[2])
			if trash == "ROTTEN_TOMATOES":
				self.notify_observers(self.possible_states[1])
		else:
			self.notify_observers(self.possible_states[0])			


	def notify_observers(self, arg):
	  	print "The garbage is now ",arg
	  	super(GarbageBin,self).notify_observers(arg)		

	def wash_bin(self):pass
