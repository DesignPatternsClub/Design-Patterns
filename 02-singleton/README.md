# Singleton (creational pattern)


### Intent

Restricts the instantiation of a class to _one object_.
This is useful when exactly one object is needed (or advised) to coordinate
actions across the system. This way we concentrate important actions into a
single point in order to provide organisation and avoid some issues.


### Key implementation characteristics

1. **Private attribute in the instance class**. This is where the reference for
the initialised instance will be kept.
2. **Public method to access the instance**. Accessor interface used to request
a reference to an instance of this class.
3. **Lazy initialisation**. Create a class instance on the first use in
the accessor method.
4. **Hide public constructors**. External entites should only get your class
instance through the accessor method, not a regular constructor.


### Examples

[Singleton pattern examples folder](https://github.com/DesignPatternsClub/Design-Patterns/tree/master/02-singleton/examples).

JavaScript: `$ node singleton.js`

Python: `$ python singleton.py`
