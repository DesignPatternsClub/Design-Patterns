
class Observable(object):
    def __init__(self):
        self.__observers = []
 
    def register_observer(self, observer): 		#observer wants
    	if observer not in self.__observers:
    		print "A registration to observe was added"
        	self.__observers.append(observer)
 
    def unregister_observer(self, observer): 		#observer wants
    	if observer in self.__observers:
   			print "A registration to observe was removed"
			self.__observers.remove(observer)
 
    def notify_observers(self, arg):
        for observer in self.__observers:
            observer.notify( arg)			#For python, Wikipedia code contains *args,*kwargs instead of just args 