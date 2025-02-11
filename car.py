from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        """Check if car needs service."""
        return self.engine.needs_service() or self.battery.needs_service()
