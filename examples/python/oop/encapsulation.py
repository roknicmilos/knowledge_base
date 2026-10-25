"""
Encapsulation is a concept that restricts access to certain
details of an object and only exposes what is necessary,
like a protective shield.

The main goal of encapsulation is to protect the internal
state of an object and ensure that the object’s methods are
used to manipulate that state in a controlled manner.

Encapsulation is achieved with access modifiers (private,
protected, public), getter and setter.
"""


class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute
        self.__bank_account = 1000  # Private attribute

    def display_name(self):
        """
        Public method
        """
        return self.name

    def _display_age(self):
        """
        Protected method, but it CAN be accessed from outside the class
        """
        return self._age

    def __display_bank_account(self):
        """
        Private method, but it CAN be accessed from outside the class
        by appending the class name to it (_ClassName__method_name).
        If tried to access it directly (obj.__display_bank_account()),
        it will raise an AttributeError.
        """
        return self.__bank_account

    def access_private_method(self):
        """
        Public method that accesses a private method
        """
        return self.__display_bank_account()
