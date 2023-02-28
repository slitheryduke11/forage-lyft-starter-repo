from car import Car
from engine.types.capulet_engine import CapuletEngine
from battery.types.nubbin_battery import NubbinBattery


class Thovex(Car):
    """Rorschach model."""
    
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        super().__init__(engine, battery)

    def needs_service(self):
        """Check if car needs service."""
        return super().needs_service()
