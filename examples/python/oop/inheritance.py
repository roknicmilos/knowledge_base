"""
Inheritance allows a class (child) to inherit properties and
methods from another class (parent), promoting code reuse.
"""


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
