"""
Proxy Pattern

What it does:
    Provides a surrogate or placeholder for another object to control
    access to it for purposes such as lazy initialization, access control,
    logging, or caching.

Non-pattern alternative: Modifying the original code
    Modifying the original code violates the Open-Closed Principle (OCP)
    and Single Responsibility Principle (SRP). Proxy pattern introduces
    a new proxy class that implements the same interface as the original
    class, thus respecting OCP and SRP. The proxy class holds a reference
    to the original object and controls access to it.
"""

from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_from_disk()  # Heavy operation

    def _load_from_disk(self):
        print(
            f"[{self.__class__.__name__}] Loading "
            f"{self.filename} from disk... (expensive operation)"
        )

    def display(self):
        print(f"[{self.__class__.__name__}] Displaying {self.filename}")


class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None  # Lazy initialization

    def display(self):
        if self._real_image is None:
            print(
                f"[{self.__class__.__name__}] "
                "Creating RealImage on first display"
            )
            self._real_image = RealImage(self.filename)
        print(f"[{self.__class__.__name__}] Delegating to RealImage")
        self._real_image.display()


if __name__ == "__main__":
    # Using ProxyImage - no immediate loading
    image1 = ProxyImage("photo1.jpg")
    image2 = ProxyImage("photo2.jpg")

    print("\nFirst display (triggers loading):")
    image1.display()  # Loads and displays

    print("\nSecond display (already loaded):")
    image1.display()  # Just displays, no reload

    print("\nDisplaying another image:")
    image2.display()  # Loads its own RealImage
