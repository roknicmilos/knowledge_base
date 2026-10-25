"""
Adapter Pattern

What it does:
    Allows incompatible interfaces to work together by
    wrapping an existing class with a new interface.

Non-pattern alternative: Modifying the original code
    Modifying the original code to match the expected interface violates
    the Open-Closed Principle (OCP) and may not be feasible if the
    original class is part of a third-party library or legacy code. The
    Adapter pattern introduces a new adapter class that implements the
    expected interface and holds a reference to the original class, thus
    respecting OCP.
"""

import math


class RoundHole:
    def __init__(self, radius: float):
        self.radius = radius

    def fits(self, peg):
        return peg.get_radius() <= self.radius


class RoundPeg:
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius


class SquarePeg:
    """Legacy/incompatible class."""

    def __init__(self, width: float):
        self.width = width

    def get_width(self) -> float:
        return self.width


class SquarePegAdapter(SquarePeg):
    """Adapter to make SquarePeg compatible with RoundHole."""

    def get_radius(self) -> float:
        # Calculate the equivalent radius (half the diagonal)
        return self.get_width() * math.sqrt(2) / 2


if __name__ == "__main__":
    hole = RoundHole(5.0)

    # Native round peg works directly
    round_peg = RoundPeg(4.0)
    print("Round peg fits:", hole.fits(round_peg))  # True

    # Small square peg (adapted)
    small_square_adapter = SquarePegAdapter(4.0)
    print(
        "Small square (with adopter) peg fits:",
        hole.fits(small_square_adapter)
    )  # True (diagonal/2 ≈ 2.828 < 5)

    # Large square peg (adapted)
    large_square_adapter = SquarePegAdapter(10.0)
    print(
        "Large square (with adopter) peg fits:",
        hole.fits(large_square_adapter)
    )  # False (diagonal/2 ≈ 7.07 > 5)

    # Legacy square peg without adapter (will fail)
    print("Attempting to fit legacy square peg without adapter:")
    legacy_square = SquarePeg(6.0)
    hole.fits(legacy_square)  # AttributeError
