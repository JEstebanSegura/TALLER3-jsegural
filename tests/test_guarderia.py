import unittest
from models.guarderia import Guarderia

class TestGuarderia(unittest.TestCase):
    def setUp(self):
        self.guarderia = Guarderia()
    
    def test_feed_boa_succes(self):
        result_test = self.guarderia.feed_boa(self.guarderia.boa1) 
        self.assertEqual(result_test, "Éxito")
    
    def test_alimentar_boa_full(self):
        for _ in range(10):
            self.guarderia.boa1.eat_mouse()
        result_test = self.guarderia.feed_boa(self.guarderia.boa1)
        self.assertEqual(result_test, "La boa está llena")
    
    def test_alimentar_boa_no_exist(self):
        result_test = self.guarderia.feed_boa(None)
        self.assertEqual(result_test, "Esta Boa no existe!")


if __name__ == '__main__':
    unittest.main