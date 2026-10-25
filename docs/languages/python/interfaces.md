# Interfaces in Python

Python has no `interface` keyword like Java/C#, but you can get the same behavior in three ways.

## 1. Duck typing (the Pythonic way)

"If it behaves like an interface, it is one."

```python
class Dog:
    def speak(self): return "woof"

class Cat:
    def speak(self): return "meow"

def make_sound(animal):
    print(animal.speak())

make_sound(Dog())
make_sound(Cat())
```

✔ no inheritance needed ✔ very flexible ✖ no enforcement (errors only at runtime)

## 2. Abstract Base Classes (`abc`) – closest to real interfaces

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self): ...

class Dog(Animal):
    def speak(self): return "woof"

class Fish(Animal):   # forgets to implement speak
    pass

Fish()
# TypeError: Can't instantiate abstract class Fish without an implementation for abstract method 'speak'
# (Python < 3.12 wording: "...with abstract method speak")
```

✔ enforced at instantiation ✔ clear contract ✔ widely used in larger systems

## 3. Protocols (structural typing, Python 3.8+)

From `typing` (`typing_extensions` on older versions) – the closest to modern interfaces / TypeScript interfaces.

```python
from typing import Protocol

class Animal(Protocol):
    def speak(self) -> str: ...

class Dog:
    def speak(self) -> str:
        return "woof"

def make_sound(animal: Animal):
    print(animal.speak())

make_sound(Dog())
```

✔ no inheritance needed ✔ works with type checkers (mypy, pyright) ✖ only checked statically – unless you decorate the
protocol with `@runtime_checkable` to allow `isinstance()` checks (which only verify method presence).

## When to use what

| Approach    | Use when                                                        |
|-------------|-----------------------------------------------------------------|
| Duck typing | Quick scripts, simple logic – behavior matters                  |
| ABC         | You want strict runtime enforcement – inheritance + enforcement |
| Protocol    | Modern, type-safe but flexible code – structure matters         |
