"""
Observer Pattern

What it does:
    Defines a one-to-many dependency between objects so that when one object
    changes state, all its dependents are notified and updated automatically.

Non-pattern alternative: Tight coupling
    Without the Observer pattern, subjects and observers would be tightly
    coupled. The subject would need to know details about its observers,
    making it difficult to add or remove observers without modifying the
    subject. This violates the Open-Closed Principle (OCP) as changes to
    observers would require changes to the subject. The Observer pattern
    decouples subjects and observers, allowing them to vary independently.
"""
from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(
        self,
        temperature: float,
        humidity: float,
        pressure: float
    ) -> None: ...


# Subject abstract class
class Subject(ABC):
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    @abstractmethod
    def notify_observers(self) -> None: ...


# Concrete Subject: WeatherData
class WeatherData(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    # Called when new measurements arrive
    def measurements_changed(self) -> None:
        self.notify_observers()

    # Simulate new data
    def set_measurements(
        self,
        temperature: float,
        humidity: float,
        pressure: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()


# Concrete Observers (displays)
class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data: Subject) -> None:
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        weather_data.register_observer(self)

    def update(
        self,
        temperature: float,
        humidity: float,
        pressure: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        print(
            f"Current conditions: {self._temperature}°C "
            f"and {self._humidity}% humidity"
        )


class StatisticsDisplay(Observer):
    def __init__(self, weather_data: Subject) -> None:
        self._temperatures: List[float] = []
        weather_data.register_observer(self)

    def update(
        self,
        temperature: float,
        humidity: float,
        pressure: float
    ) -> None:
        self._temperatures.append(temperature)
        self.display()

    def display(self) -> None:
        if self._temperatures:
            avg_temp = sum(self._temperatures) / len(self._temperatures)
            print(
                f"Avg temperature: {avg_temp:.1f}°C "
                f"(based on {len(self._temperatures)} readings)"
            )


if __name__ == "__main__":
    _weather_data = WeatherData()

    stats_display = StatisticsDisplay(_weather_data)
    print("--- New measurements ---")
    _weather_data.set_measurements(25.5, 65, 1013)

    current_display = CurrentConditionsDisplay(_weather_data)
    print("\n--- New measurements ---")
    _weather_data.set_measurements(27.0, 70, 1010)

    _weather_data.remove_observer(stats_display)
    print("\n--- New measurements ---")
    _weather_data.set_measurements(23.8, 90, 1005)
