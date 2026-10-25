# Python examples

This repository contains examples of various Python
features and libraries. It also contains Python examples
of general programming concepts.

## Table of Contents

- [Iterators and Iterables](./iterations/README.md)
- [Object-Oriented Programming](./oop/README.md)
- [Big O Notation](./bigO/README.md)
   
- [Design Patterns](./design_patterns/README.md)

## Running

Run from this directory so the package imports resolve:

```bash
cd examples/python
python -m bigO.o_n
python -m iterations.iterables.iterable
# dependency-injection examples import `helpers.*`, so run them from their own folder
cd design_patterns/dependency_injection/examples && python di_w_interfaces.py
```
