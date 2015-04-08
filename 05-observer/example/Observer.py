from Observable import Observable

class Observer(object):
    def __init__(self, observable):
    	print "Registering.."
        observable.register_observer(self)
 
    def notify(self, args):
        print('Got', args,)
 

