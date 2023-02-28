from engine.engine import Engine


class SternmanEngine(Engine):
    """Sternman engine."""

    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        """Check if engine needs service."""
        return self.warning_light_is_on
