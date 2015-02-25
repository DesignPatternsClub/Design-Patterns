Outline for the Strategy Pattern presentation
=====

## Outline

1. What's a Design Pattern?
2. Kinds of Design Patterns (behavioral, creational, structural)
3. What is a Strategy Pattern? (short intro)
4. `list1` in *string_lists.py*: short list of strings to parse
5. *example1.py*: if-elif-else approach (for parsing `list1`)
6. `list2` in *string_lists.py*: longer list of strings to parse (more special cases)
7. *example2.py*: more cases for the if-elif-else approach (for parsing `list2`)
8. *example3.py*: rework the client script for a Strategy pattern approach
9. *parsers_1.py*: encapsulating the cases into classes, in a separate module (for parsing `list1`)
10. *parsers_2.py*: add parsers using base classes to factor out the category name in parsers for the same kind of information
11. *parsers_3.py*: relocate regular expression validation code into the base class of all parsers (all parsers use same approach for validation: regular espressions) and add a `VALIDATION_PATTERN` data member into each parser class
12. *parsers_4.py*: factor out parse method of the parsers relocating it into the category base class of each parser and adding class data members with `TOKEN` and `REPLACE_STR` to be used by the parse methods
13. `list3` in *string_lists.py*: adds a few more special cases
14. *parsers_5.py*: show how easy is to add new parsers for the new special cases (for parsing `list3`)
15. Discuss benefits of one approach over the other one

## What the example does?

There are list of strings (*string_lists.py*) with information to be parsed as id-description pairs. The parser will extract the information and return it in a dictionary with key = id and value = description, plus an indication of what kind of information (category) is this about.

In the example the result is just stored in a dictionary of lists, with a list for each kind of information and printed.

*Structure of the result dictionary*

{'category1': [{'desc': 'any_description', 'id': 'any_id'},
               {'desc': 'any_description', 'id': 'any_id'}],
 'category2': [{'desc': 'any_description', 'id': 'any_id'},
               {'desc': 'any_description', 'id': 'any_id'}],
 'category3': [{'desc': 'any_description', 'id': 'any_id'},
               {'desc': 'any_description', 'id': 'any_id'}]
}