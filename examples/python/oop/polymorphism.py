"""
Polymorphism describes the concept that you can access objects
of different types through the same interface.
Each type can provide its own independent implementation of this
interface.
"""

from abc import abstractmethod


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
    """
    This function expects an instance of a class that implements
    the say_hello method. It doesn't care about the specific class
    that is passed in, as long as it has the say_hello method.
    """
    return person.say_hello()
