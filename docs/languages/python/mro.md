# Method Resolution Order (MRO)

The order in which Python searches a class hierarchy for a method or attribute – especially relevant with multiple
inheritance.

## Key points

1. Python 3 uses the **C3 linearization** algorithm.
2. It guarantees:
    - a child class is checked before its parents,
    - with multiple bases, they're checked left to right,
    - each class appears only once.
3. Inspect it with `Class.mro()` or `Class.__mro__`.

## Example

```python
class A:
    def method(self): print("A")

class B(A):
    def method(self): print("B")

class C(A):
    def method(self): print("C")

class D(B, C):
    pass

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

Lookup order: `D` → `B` → `C` → `A` → `object`. `super()` follows this order too.

## Why it matters

- Avoids ambiguity in multiple inheritance (clear lookup path).
- Consistent method lookup across the hierarchy.
