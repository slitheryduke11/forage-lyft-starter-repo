import datetime

from battery.battery import Battery


class NubbinBattery(Battery):
    """Nubbin battery."""

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.years_for_service = 4

    def needs_service(self):
        """Check if battery needs service."""
        date_for_service = self.last_service_date.replace(year=self.last_service_date.year + self.years_for_service)
        return date_for_service < datetime.date.today()
