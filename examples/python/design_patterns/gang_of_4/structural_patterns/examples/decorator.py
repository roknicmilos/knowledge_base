"""
Decorator Pattern

What it does:
    Allows behavior to be added to individual objects, either statically
    or dynamically, without affecting the behavior of other objects from
    the same class. It achieves this through composition, by wrapping the
    original object in one or more decorator classes that conform to the
    same interface and delegate calls while enhancing functionality.

Non-pattern alternative: Inheritance
    Inheritance supports Open-Closed Principle (OCP), but can lead to
    class explosion or rigid hierarchies. Decorator Pattern provides
    greater flexibility by allowing behaviors to be mixed and matched at
    runtime.
    For example, if we have a base class A, and extensions B, C, and D
    then using inheritance would require creating subclasses for every
    possible combination (e.g., A with B, A with C, A with C, A with B&C,
    A with B&D, etc.), leading to a combinatorial explosion of classes.
    In contrast, with the Decorator Pattern, we can create decorators for
    B, C, and D separately and then wrap instances of A with any combination
    of these decorators at runtime, significantly reducing the number of
    classes needed and enhancing flexibility.
"""
from abc import abstractmethod, ABC


class Vehicle(ABC):

    @abstractmethod
    def start(self) -> str: ...

    @abstractmethod
    def drive(self) -> str: ...

    @abstractmethod
    def stop(self) -> str: ...

    @abstractmethod
    def get_features(self) -> list[str]: ...


class Car(Vehicle):

    def start(self) -> str:
        return "Car has started."

    def drive(self) -> str:
        return "Car is being driven."

    def stop(self) -> str:
        return "Car has stopped."

    def get_features(self) -> list[str]:
        return ["Standard"]


class VehicleDecorator(Vehicle):
    """
    Base Decorator class that wraps a Vehicle object.
    It delegates all operations to the wrapped object.
    """

    def __init__(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def start(self) -> str:
        return self._vehicle.start()

    def drive(self) -> str:
        return self._vehicle.drive()

    def stop(self) -> str:
        return self._vehicle.stop()

    def get_features(self) -> list[str]:
        return self._vehicle.get_features()


class SportCarDecorator(VehicleDecorator):

    def start(self) -> str:
        result = super().start()
        return f"\t>>> Sport mode activated!\n{result}"

    def stop(self) -> str:
        result = super().stop()
        result += "\n\t>>> Sport mode deactivated."
        return result

    def get_features(self) -> list[str]:
        return super().get_features() + ["Sport"]


class LuxuryCarDecorator(VehicleDecorator):

    def start(self) -> str:
        result = super().start()
        return f"\t$$$ Luxury features enabled.\n{result}"

    def stop(self) -> str:
        result = super().stop()
        result += "\n\t$$$ Luxury features disabled."
        return result

    def get_features(self) -> list[str]:
        return super().get_features() + ["Luxury"]


if __name__ == "__main__":
    config = {
        "has_sport_package": True,
        "has_luxury_package": True,
    }

    car = Car()
    if config["has_sport_package"]:
        car = SportCarDecorator(car)
    if config["has_luxury_package"]:
        car = LuxuryCarDecorator(car)

    print(f"\nFeatures: {', '.join(car.get_features())}\n")

    print(car.start())
    print(car.drive())
    print(car.stop())

    print(f"\nObject type: {car.__class__.__name__}")
    print(
        f"Inheritance tree: "
        f"{' => '.join(c.__name__ for c in car.__class__.__mro__)}"
    )
    level = 1
    if hasattr(car, "_vehicle"):
        vehicle_type = car._vehicle.__class__.__name__
        while vehicle_type:
            print(f"\t{'> ' * level} Wrapped vehicle type: {vehicle_type}")

            if not hasattr(car._vehicle, "_vehicle"):
                break

            car = car._vehicle
            vehicle_type = car._vehicle.__class__.__name__
            level += 1
