from abc import abstractmethod
from models.ianimal import iAnimal

class Animal(iAnimal):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilograms_eaten = 0

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str):
            self._nombre = value

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

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if isinstance(value, int):  # ✅ Solo entra si es entero
            if value >= 0:
                self._edad = value
            else:
                raise ValueError("Value Error")
        else:
            raise TypeError("Type Error")
    
    def eat(self, kilogram: float)-> None:
        self._kilograms_eaten+=kilogram

    def kilograms_eaten(self)-> float:
        return self._kilograms_eaten

    @abstractmethod
    def make_sound(self):
        pass
    