import unittest

from tires.carrigan import CarriganTires
from tires.octoprime import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_carrigan_tires_should_be_serviced(self):
        tire_wear_readings = [0.8, 0.1, 0.9, 0.5]
        tires = CarriganTires(tire_wear_readings)
        self.assertTrue(tires.needs_service())
    
    def test_carrigan_tires_should_not_be_serviced(self):
        tire_wear_readings = [0.8, 0.1, 0.7, 0.5]
        tires = CarriganTires(tire_wear_readings)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_octoprime_tires_should_be_serviced(self):
        tire_wear_readings = [0.8, 0.2, 1, 1]
        tires = OctoprimeTires(tire_wear_readings)
        self.assertTrue(tires.needs_service())
    
    def test_octoprime_tires_should_not_be_serviced(self):
        tire_wear_readings = [0.8, 0.1, 0.7, 0.5]
        tires = OctoprimeTires(tire_wear_readings)
        self.assertFalse(tires.needs_service())