# Observer Pattern
## Intent
A nice way to decouple an object that has changing state from objects who want to know about that object's state. The objects who want to observe can stop or start observing at any time. 

### Commonly Used
While implementing MVC, the model usually becomes an observable object while the View is the observer.
Events and EventHandlers are a kind of language implementation of observer.
In distributed event handling.

### Some problems
Observers need to be disciplined about unregistering themselves if they dont want to observe anymore
One Observer can stall notifications to other observers
