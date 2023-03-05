import unittest

from tires.types.carrigan_tires import CarriganTires
from tires.types.octoprime_tires import OctoprimeTires


class TestCarrigan(unittest.TestCase):
	def test_should_be_serviced(self):
		tires_wear = [0.9, 0, 0, 0]
		tires = CarriganTires(tires_wear)
		self.assertTrue(tires.needs_service())

	def test_should_not_be_serviced(self):
		tires_wear = [0, 0, 0, 0]
		tires = CarriganTires(tires_wear)
		self.assertFalse(tires.needs_service())

class TestOctoprime(unittest.TestCase):
	def test_should_be_serviced(self):
		tires_wear = [1, 1, 1, 0]
		tires = OctoprimeTires(tires_wear)
		self.assertTrue(tires.needs_service())

	def test_should_not_be_serviced(self):
		tires_wear = [0, 0, 0, 0]
		tires = OctoprimeTires(tires_wear)
		self.assertFalse(tires.needs_service())
