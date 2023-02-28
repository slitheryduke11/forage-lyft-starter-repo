from car import Car
from engine.types.willoughby_engine import WilloughbyEngine
from battery.types.spindler_battery import SpindlerBattery


class Glissade(Car):
    """Glissade model."""
    
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        super().__init__(engine, battery)

    def needs_service(self):
        """Check if car needs service."""
        return super().needs_service()
