# OOP

Object-Oriented Programming is a paradigm centered around **objects** rather than functions and procedures.

**Two key components**

- **Objects** – real-world-like entities with attributes (data) and behaviors (methods).
- **Classes** – blueprints for creating objects.

## Four principles

### Inheritance

A child class inherits properties and methods from a parent class, promoting reuse.

```python
class Animal:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")


class Dog(Animal):
    def run(self):
        print("Running...")

    def bark(self):
        print("Barking...")


class Bird(Animal):
    def fly(self):
        print("Flying...")

    def sing(self):
        print("Singing...")
```

### Encapsulation

Restrict access to an object's internals and expose only what is necessary, so its state is only changed through its
methods. Achieved with access modifiers (C#, Java), properties (C#, Python), getters/setters and methods.

```python
class Person:
    def __init__(self, name, age):
        self.name = name             # public
        self._age = age              # "protected" – convention only
        self.__bank_account = 1000   # "private" – name-mangled to _Person__bank_account

    def display_name(self):
        return self.name

    def _display_age(self):          # protected by convention, still reachable from outside
        return self._age

    def __display_bank_account(self):  # name-mangled; obj.__display_bank_account() raises AttributeError
        return self.__bank_account

    def access_private_method(self):
        return self.__display_bank_account()
```

### Polymorphism

Objects of different types are used through the same interface; each type provides its own implementation.

```python
class Serbian:
    def say_hello(self):
        return "Ćeo"

class Croatian:
    def say_hello(self):
        return "Bok"

class Englishman:
    def say_hello(self):
        return "Hello"

def introduce(person):
    # doesn't care about the concrete class, only that it has say_hello()
    return person.say_hello()
```

### Abstraction

Reduce complexity by hiding unnecessary details and exposing only the essential characteristics – *what* an object does,
not *how*. Done with interfaces or abstract classes that define signatures without implementation.

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self): ...


class Dog(Animal):
    def speak(self):
        return "Woof!"


def animal_sound(animal: Animal):
    return animal.speak()
```

(The original repo example uses `@abstractmethod` without inheriting from `ABC`, which does **not** enforce anything.)

Source examples: <https://github.com/roknicmilos/python-stuff/tree/main/oop>

## Inheritance across languages

|                         | Python                                              | JavaScript (prototype-based)  | PHP                                     |
|-------------------------|-----------------------------------------------------|-------------------------------|-----------------------------------------|
| Syntax                  | `class Child(Parent)`                               | `class Child extends Parent`  | `class Child extends Parent {}`         |
| Multiple inheritance    | Yes (C3 MRO, see [MRO](../languages/python/mro.md)) | No (mixins possible)          | No (traits + multiple interfaces)       |
| Parent call             | `super()` (dynamic resolution)                      | `super` (bound at definition) | `parent::`                              |
| Underlying mechanism    | Class hierarchy                                     | Prototype chain (`__proto__`) | Single-parent chain + traits            |
| Access control          | Convention (`_`, `__`)                              | Convention / `#private`       | Keywords `public`/`protected`/`private` |
| Constructor inheritance | Manual (`super().__init__()`)                       | `super()` in constructor      | Manual (`parent::__construct()`)        |

See also: [SOLID](solid.md), [typing](typing.md), [Python OOP/paradigms](../languages/python/README.md).
