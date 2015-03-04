# Strategy (behavioral pattern)


### Intent

Encapsulate algorithms inside classes and make them interchangeable. The goal is to be able to add, remove and modify any number of alternative algorithms to solve a problem without changing the user interface that calls for them.


### Key implementation characteristics

1. **Base class that encapsulates user interface**. User can couple to a certain interface that will never change.
2. **Algorithms implementation encapsulated in families of classes**. There can be any number of derived classes and related algorithms should inherit common behavior or data from base classes.
3. **No impact to the user when number or implementation of derived classes change**. The user shouldn't need to know the algorithms number, names or implementation details.


### Examples

[Strategy pattern examples folder](https://github.com/DesignPatternsClub/Design-Patterns/tree/master/01-strategy/examples)


