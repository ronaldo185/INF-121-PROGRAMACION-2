from abc import ABC, abstractmethod
from typing import Protocol
import random
import math

class Coloreado(ABC):
    def como_colorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color: str):
        self.color = color
    def set__color(self, color: str):
        self.color = color
    def get__color(self) -> str:
        return self.color
    
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass
    def __str__(self) -> str:
        return f"Color: {self.color}"
    
# subclases
class Circulo(Figura):
    def __init__(self, radio: float, color: str):
        super().__init__(color)
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio
    
    def como_colorear(self) -> str:
        return "Colorear toda la superficie"

    def __str__(self) -> str:
        return f"Círculo - {super().__str__()}, Radio: {self.radio}"
    
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str):
        super().__init__(color)
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado

    def como_colorear(self) -> str:
        return "Colorear toda la superficie"

    def __str__(self) -> str:
        return f"Cuadrado - {super().__str__()}, Lado: {self.lado}"
    
def main():
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja"]
    Figuras: list[Figura] = []

    for _ in range(5):
        tipo = random.choice(['1', '2'])
        color = random.choice(colores)
        if tipo == '1':
            lado = 1 + random.random() * 9
            Figuras.append(Cuadrado(lado, color))
        else:
            radio = 1 + random.random() * 5
            Figuras.append(Circulo(radio, color))

    print("=== Lista de Figuras ===")
    for figura in Figuras:
        print(figura)
        print(f"Área: {figura.area()}")
        print(f"Perímetro: {figura.perimetro()}")
        print(f"Cómo colorear: {figura.como_colorear()}")
        if isinstance(figura, Coloreado):
            print(f"Cómo colorear (Coloreado): {figura.como_colorear()}")
        print("-" * 27)
