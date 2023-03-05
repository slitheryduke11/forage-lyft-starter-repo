from tires.tires import Tires


class CarriganTires(Tires):
    """Carrigan tires."""

    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        """Check if tires needs service."""
        for value in self.tires_wear:
            if value >= 0.9:
                return True
        return False
