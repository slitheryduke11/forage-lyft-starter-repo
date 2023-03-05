import unittest

from engine.types.capulet_engine import CapuletEngine
from engine.types.sternman_engine import SternmanEngine
from engine.types.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
	def test_should_be_serviced(self):
		current_mileage = 30002
		last_service_mileage = 1
		engine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertTrue(engine.needs_service())

	def test_should_not_be_serviced(self):
		current_mileage = 30002
		last_service_mileage = 2
		engine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
	def test_should_be_serviced(self):
		warning_light_is_on = True
		engine = SternmanEngine(warning_light_is_on)
		self.assertTrue(engine.needs_service())

	def test_should_not_be_serviced(self):
		warning_light_is_on = False
		engine = SternmanEngine(warning_light_is_on)
		self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
	def test_should_be_serviced(self):
		current_mileage = 60002
		last_service_mileage = 1
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertTrue(engine.needs_service())

	def test_should_not_be_serviced(self):
		current_mileage = 60002
		last_service_mileage = 2
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertFalse(engine.needs_service())
