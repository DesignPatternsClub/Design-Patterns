title: Singleton pattern
author:
    name: Gonçalo Morais
    twitter: gnclmorais
    url: http://gnclmorais.com
output: presentation.html
controls: false

--

# The Singleton Pattern
## ~ Design Patterns study group ~

--

### Wikipedia

> _In software engineering, the singleton pattern is a design pattern that_
> _restricts the instantiation of a class to **one object**. This is useful when_
> _exactly **one object** is needed to coordinate actions across the system._
> _The concept is sometimes generalized to systems that operate more efficiently_
> _when only **one object** exists, or that restrict the instantiation to a certain_
> _number of objects._

--

### Purpose

> ## _One Instance to rule them all,_
> ## _One Instance to find them,_
> ## _One Instance to bring them all_
> ## _and in the code bind them (…)_

--

### Good cases

+ Loggers
+ Factories
+ Network interfaces
+ Database reader/writer
+ System/application state
+ …

--

### Example — Java

```java
public class SingletonDemo {
    private static SingletonDemo instance = null;

    private SingletonDemo() {…}
 
    public static SingletonDemo getInstance() {
        if (instance == null) {
            instance = new SingletonDemo();
        }
 
        return instance;
    }
}
```

--

### Example — JavaScript

```javascript
var mySingleton = (function () {
    var instance;
 
    function init() {
        var privateVariable = "I’m private";

        function privateMethod() {…}
 
        return {
            publicProperty: "I am public",
            publicMethod: function () {…}
        };
    };
 
    return {
        getInstance: function () {
            if (!instance) {
                instance = init();
            }
 
            return instance;
        }
    };
})();
```

--

### Example — Python

```python
class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)
```

--

### Further reading

+ In general:  
  http://sourcemaking.com/design_patterns/singleton  

+ Python:  
  http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Singleton.html  
  
+ JavaScript:  
  http://addyosmani.com/resources/essentialjsdesignpatterns/book/#singletonpatternjavascript
