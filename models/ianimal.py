from abc import ABC, abstractmethod

class iAnimal(ABC):

    @abstractmethod       
    def eat(self, kilogram: float)-> None:
        pass

    @abstractmethod
    def kilograms_eaten(self)-> float:
        pass   
    