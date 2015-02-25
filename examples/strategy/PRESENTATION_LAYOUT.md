Layout for the Strategy Pattern presentation
=====

## Sequence

1. What's a Design Pattern?
2. Kinds of Design Patterns
3. What is a Strategy Pattern?
4. Example 1: short list of strings to parse
5. Example 1: if-elif-else approach
6. Example 2: longer list of strings to parse (growing cases)
7. Example 2: more cases for the if-elif-else approach
8. Example 3: encapsulating cases into classes, in other module
9. Example 4: even longer list of strings to parse (growing cases)
10. Example 4: just adding new class encapsulated cases
11. Discuss benefits of one approach over the other one

## What the example does?

There is a list of strings with information to be parsed. The parser will extract the information and returned it in a dictionary with proper key-tagging plus an indication of what kind of information is this about.

In the example the result is just printed out as it goes and stored in a dictionary of lists, with a list for each kind of information, but a more realistic scenario would be that the main routine stores the parsed information in a database.