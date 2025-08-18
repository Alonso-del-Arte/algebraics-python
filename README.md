# Algebraics, Python

WORK IN PROGRESS. This is for algebraic number theory, such as imaginary 
quadratic rings, pure cubic numbers and so on and so forth.

This is similar to my algebraic integer calculator project in Java. The 
conceptual differences due to Java being strongly typed and Python not being as 
strongly typed might not be as great as I imagined.

I might be duplicating effort that has already been made for Python. But if 
nothing else, this will help me understand object-oriented programming in 
Python.

As I figure out what is idiomatic in Python, I will do a lot of things the way I
do them in Java, which might not always be proper Python. The most obvious of 
these pertain to naming conventions.

Far more importantly, however, the concept of inheritance, even with relatively 
shallow inheritance hierarchies, is turning out to be more difficult than I 
expected, such as the differences with abstract classes and the singleton 
pattern.

Note to self: Run tests at project root level with

```
python3 -m test.ringstest
```

replacing `ringstest` when necessary.
