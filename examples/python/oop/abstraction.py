"""
Abstraction is a concept we use for reducing complexity by
hiding the unnecessary details and highlighting the essential
characteristics.

It focuses on exposing only the relevant aspects of an object,
making it easier to use and understand.

Abstraction involves using interfaces or abstract classes to
define and enforce method signatures without specifying their
implementation.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


def animal_sound(animal: Animal):
    """
    This function expects an instance of a class that implements
    the speak method. It doesn't care about the implementation
    details, as long as the class has the speak method.
    """
    return animal.speak()
