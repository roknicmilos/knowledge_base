"""
Builder Pattern

What it does:
    Separates the construction of a complex object from its
    representation, allowing the same construction process to
    create different representations.

Non-pattern alternative: Telescoping constructor
    Using a telescoping constructor with multiple parameters
    can lead to code that is hard to read and maintain. The Builder
    pattern provides a clear and fluent interface for constructing
    complex objects step by step, improving code readability and
    maintainability.
"""

from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.foundation = ''
        self.structure = ''
        self.roof = ''
        self.furnished = False

    def __str__(self):
        parts = [self.foundation, self.structure, self.roof]
        if self.furnished:
            parts.append('furnished')
        return 'House with ' + ', '.join(filter(None, parts))


class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    def reset(self):
        self.house = House()

    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    def build_furniture(self):
        pass  # Optional step

    def get_result(self):
        return self.house


class IglooBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = 'ice block foundation'

    def build_structure(self):
        self.house.structure = 'ice block walls'

    def build_roof(self):
        self.house.roof = 'ice dome'


class CastleBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = 'stone foundation'

    def build_structure(self):
        self.house.structure = 'stone walls'

    def build_roof(self):
        self.house.roof = 'towers'

    def build_furniture(self):
        self.house.furnished = True


class Director:
    """
    The Director's primary role is to encapsulate a specific
    construction algorithm that can be reused across different
    builders (e.g., directing "build minimal viable object" vs.
    "build fully featured object"). With just one concrete builder,
    that separation adds unnecessary indirection and an extra class
    without real benefit. In other words, the Director isn't
    necessarily when there's only one builder. In such cases, the
    client code can directly use the builder to construct the object.
    """

    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.reset()
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_furniture()


if __name__ == "__main__":
    director = Director()

    igloo_builder = IglooBuilder()
    director.set_builder(igloo_builder)
    director.construct()
    igloo = igloo_builder.get_result()
    print("Igloo:", igloo)

    castle_builder = CastleBuilder()
    director.set_builder(castle_builder)
    director.construct()
    castle = castle_builder.get_result()
    print("Castle:", castle)
