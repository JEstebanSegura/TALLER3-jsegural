from models.boa_constrictor import BoaConstrictor
from models.huron import Huron

class Guarderia:
    def __init__(self):
        self.boa1 = BoaConstrictor("Boa1", 15.0, 5, "Brasil", 20.0)
        self.boa2 = BoaConstrictor("Boa2", 12.0, 4, "Ecuador", 18.0)
        self.huron1 = Huron("Huron1", 2.5, 3, "Argentina", 10.0)
        self.huron2 = Huron("Huron2", 3.0, 2, "Chile", 12.0)
    
    def feed_boa(self, boa: BoaConstrictor):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.eat_mouse() 
            return "Éxito" 
        except ValueError:
            return "La boa está llena"