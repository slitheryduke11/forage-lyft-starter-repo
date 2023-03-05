import unittest
from datetime import date

from battery.types.nubbin_battery import NubbinBattery
from battery.types.spindler_battery import SpindlerBattery


class TestNubbin(unittest.TestCase):
	def test_should_be_serviced(self):
		last_service_date = date.today()
		last_service_date = last_service_date.replace(year=last_service_date.year - 5)
		battery = NubbinBattery(last_service_date)
		self.assertTrue(battery.needs_service())

	def test_should_not_be_serviced(self):
		last_service_date = date.today()
		battery = NubbinBattery(last_service_date)
		self.assertFalse(battery.needs_service())

class TestSpindler(unittest.TestCase):
	def test_should_be_serviced(self):
		last_service_date = date.today()
		last_service_date = last_service_date.replace(year=last_service_date.year - 3)
		battery = SpindlerBattery(last_service_date)
		self.assertTrue(battery.needs_service())
		
	def test_should_not_be_serviced(self):
		last_service_date = date.today()
		battery = SpindlerBattery(last_service_date)
		self.assertFalse(battery.needs_service())
