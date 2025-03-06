from models.animal_exotico import AnimalExotico

class Huron(AnimalExotico):

    def __init__(self, nombre: str, peso: float, edad: int, country_origin: str, taxes: float):
        super().__init__(nombre, peso, edad, country_origin, taxes)
    
    def make_sound(self):
       return "¡Eek Eek!"