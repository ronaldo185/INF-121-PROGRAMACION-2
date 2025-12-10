from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):
        self._nombre = nombre

    @abstractmethod
    def calcular_salario_mensual(self):
        pass

    def __str__(self):
        return f"Nombre: {self._nombre}"

    @property
    def nombre(self):
        return self._nombre
