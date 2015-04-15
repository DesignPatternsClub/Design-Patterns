# Memento Pattern

> Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later. -- [Design Patterns: Elements of Reusable Object-Oriented Software](http://www.uml.org.cn/c++/pdf/DesignPatterns.pdf)


The core intent is to capture an object's internal state (for later restoration) without violating encapsulation (i.e. uncovering internals for the purpose of externalization).

Therefore, the state-representing object - called the memento - should satisfy 2 criteria:

1. The memento should be opaque (aka provide no insight)
The only allowed action with a memento is to return it to its originator for the purpose of state restoration. (This one may be relaxed in some variants to allow passing of states between sibling instances.)

2. Memento is extremely useful with transactional processing semantics, i.e. when an action is expected to either entirely succeed and change the system state in a defined way, or, on failure, not to change the system state at all.

Software in the wild the utilizes this pattern:

* SQL - ability to rollback a transaction or commit it
* Git/VCS -  Ability to return to prior state if a merge/change failes
* Video games - ability to save a game at a certain point and return to that point if the power goes out etc. Or think of quick saving.


Source:

* https://wiki.python.org/moin/MementoPattern 
* http://www.uml.org.cn/c++/pdf/DesignPatterns.pdf
* https://github.com/oxnz/design-patterns/blob/master/src/memento/python/memento.py


The memento pattern is a behavioral pattern.



pg 249, 316