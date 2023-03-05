from tires.tires import Tires


class OctoprimeTires(Tires):
    """Octoprime tires."""

    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        """Check if tires needs service."""
        return sum(self.tires_wear) >= 3.0
