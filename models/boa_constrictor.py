from models.animal_exotico import AnimalExotico

class BoaConstrictor(AnimalExotico):

    def __init__(self, nombre: str, peso: float, edad: int, country_origin: str, taxes: float):
        super().__init__(nombre, peso, edad, country_origin, taxes)
        self.__mouses_eaten =0
    
    def make_sound(self):
       return "¡Tsss!"
    
    def eat_mouse(self):
        if self.__mouses_eaten >= 10:
            raise ValueError("Demasiados Ratones!")
        self.__mouses_eaten += 1

    def mouses_eaten(self)-> int:
        return self.__mouses_eaten