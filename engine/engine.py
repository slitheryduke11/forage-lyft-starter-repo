from abc import ABC, abstractmethod


class Engine(ABC):
	"""Base engine."""

	@abstractmethod
	def needs_service(self):
		"""Check if engine needs service."""
		pass
