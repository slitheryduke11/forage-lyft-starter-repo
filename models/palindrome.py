from car import Car
from engine.types.sternman_engine import SternmanEngine
from battery.types.spindler_battery import SpindlerBattery


class Palindrome(Car):
    """Palindrome model."""
    
    def __init__(self, warning_light_is_on, last_service_date):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        super().__init__(engine, battery)

    def needs_service(self):
        """Check if car needs service."""
        return super().needs_service()
