from abc import ABC, abstractmethod
from ianimal import iAnimal

class AnimalGranja(iAnimal):
    def __init__(self, peso: float):
        self._peso = peso
        self._kilograms_eaten

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, value):
        if isinstance(value, (int, float)):  
            if value > 0:
                self._peso = value
            else:
                raise ValueError("Value Error")
        else:
            raise TypeError("Type Error")

    def eat(self, kilogram: float)-> None:
        self._kilograms_eaten+=(kilogram*0,8)

    def kilograms_eaten(self)-> float:
        return self._kilograms_eaten   

    @abstractmethod
    def make_sound(self):
        pass
    

