from Observer import Observer

class RoomMate(Observer):

	def __init__(self, bin,name, is_fastidious):
		super(RoomMate,self).__init__(bin)
		self.bin = bin
		self.name = name
		self.is_fastidious = is_fastidious
		print self.name,"is now living in the houese\n"

	def arrives_home(self):
		self.bin.register_observer(self)
		print self.name, "came home and is now watching the bin"

	def leaves_home(self):
		self.bin.unregister_observer(self)

	def eating_food(self):	
		print self.name," is eating something"
		self.bin.put_trash_in("Food Container")
	
	def notify(self, args):
		print self.name,"observes that the garbage is",args
		if args == "STINKY" or args == "FULL":
			self.bin.take_out_trash()
