import unittest
from models.boa_constrictor import BoaConstrictor

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = BoaConstrictor("Boa1", 15.0, 5, "Brasil", 20.0)

    def test_make_sound(self):
        self.assertEqual(self.boa.make_sound(), "¡Tsss!")

    def test_calculate_freight(self):
        self.assertEqual(self.boa.calculate_freight(), 15.0 * 20.0)
    
    def test_eat_mouse(self):
        for _ in range(10):
            self.boa.eat_mouse()
        #aca se espera que se lance una execpcion:
        with self.assertRaises(ValueError) as e:
            self.boa.eat_mouse()
        self.assertEqual(str(e.exception), "Demasiados Ratones!")