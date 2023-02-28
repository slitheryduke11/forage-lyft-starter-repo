from abc import ABC, abstractmethod


class Battery(ABC):
    """Base battery."""

    @abstractmethod
    def needs_service(self):
        """Check if battery needs service."""
        pass
