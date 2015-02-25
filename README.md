# Design-Patterns workshop
A repository for the Design Patterns workshop at Hacker School - https://www.hackerschool.com

## Resources for studying Design Patterns

* Design Patterns: Elements of Reusable Object-Oriented Software (Gang of 4) -  http://www.uml.org.cn/c++/pdf/DesignPatterns.pdf - This will be the book accompaniment for the HS workshop
* http://sourcemaking.com/design_patterns - A friendly introduction to Design Patterns
* Design Patterns in Python (Verma, R. and Giridhar, C.) - http://kennison.name/files/zopestore/uploads/python/DesignPatternsInPython_ver0.1.pdf - Some examples of python Design Patterns implementation

*Notes for this repo have been taken from all of the sources.*

## How to use this repo

Each pattern is briefly described below and it has an examples folder. Python code for the examples is provided there, together with a *PRESENTATION_OUTLINE.md* that outlines how the example was presented in the workshop.

## Patterns

### Strategy (behavioral pattern)

*Intent*

Encapsulate algorithms inside classes and make them interchangeable. The goal is to be able to add, remove and modify any number of alternative algorithms to solve a problem without changing the user interface that calls for them.

*Key implementation characteristics*

1. **Base class that encapsulates user interface**. User can couple to a certain interface that will never change.
2. **Algorithms implementation encapsulated in families of classes**. There can be any number of derived classes and related algorithms should inherit common behavior or data from base classes.
3. **No impact to the user when number or implementation of derived classes change**. The user shouldn't need to know the algorithms number, names or implementation details.

[Strategy pattern examples folder](https://github.com/abenassi/Design-Patterns/tree/master/examples/strategy)


