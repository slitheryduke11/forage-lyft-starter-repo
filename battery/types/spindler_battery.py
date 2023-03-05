from datetime import date

from battery.battery import Battery


class SpindlerBattery(Battery):
    """Spindler battery."""

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.years_for_service = 3

    def needs_service(self):
        """Check if battery needs service."""
        date_for_service = self.last_service_date.replace(year=self.last_service_date.year + self.years_for_service)
        return date_for_service < date.today()
