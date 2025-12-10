from math import pi

class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError

    def __str__(self):
        return f"Color: {self.color}"

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2

    def perimetro(self):
        return 2 * pi * self.radio

    def __str__(self):
        return f"Circulo - {super().__str__()}, Radio: {self.radio}"
