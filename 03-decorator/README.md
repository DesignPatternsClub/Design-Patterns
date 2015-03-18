# Decorator (structural pattern)


### Intent

Add additional **behavior** or **state** to objects at run-time. It is an alternative to subclassing for extending functionality in which only specific objects get the new features (and not the entire class). Combining decorators makes possible to personalize an object adding different functionality in each case. Using decorators is also useful to remove from an object secondary functionality that therefore can be easily added or removed to the object.


### Key implementation characteristics

1. **One non optional core functionality, with one or many optional wrappers**. There is always a core function or object that does the most important task and then the "decorators" should be optional functionality that may or may not be added to the core function or object without affecting its ability to function.
2. **Client interface must not change**. The interface of the decorated function must be the same than the interface of the core function, so the client can use it in the same way.
3. **Client must be able to define type, order and number of decorators used with a single core object**. The decorators should be defined in such a way that the type, order or number of them applied to a core function or object do not break the ability to call the decorated function or object in the same way than before. Although those client decisions could change the result functionality of the decorated function or object.