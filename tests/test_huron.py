import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Huron1", 2.5, 3, "Argentina", 10.0)

    def test_make_sound(self):
        self.assertEqual(self.huron.make_sound(), "¡Eek Eek!")
        
    def test_calculate_freight(self):
        self.assertEqual(self.huron.calculate_freight(), 2.5 * 10.0)