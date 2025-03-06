from abc import ABC, abstractmethod
from models.animal import Animal

class AnimalExotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, country_origin: str, taxes: float):
        super().__init__(nombre, peso, edad)
        self.__country_origin = country_origin
        self.__taxes = taxes
        

    @property
    def country_origin(self):
        return self.__country_origin

    @country_origin.setter
    def country_origin(self, value):
        if isinstance(value, str):
            self.__country_origin = value

    @property
    def taxes(self):
        return self.__taxes

    @taxes.setter
    def taxes(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                self.__taxes = value
            else:
                raise ValueError("Value Error")
        else:
            raise TypeError("Type Error")

    def calculate_freight (self) -> float:
        return self.__taxes*self._peso
    
    #@abstractmethod
    #def make_sound(self):
    #    pass
    