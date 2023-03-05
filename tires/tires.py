from abc import ABC, abstractmethod


class Tires(ABC):
	"""Base Tires."""

	@abstractmethod
	def needs_service(self):
		"""Check if tires needs service."""
		pass
