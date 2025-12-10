class Figura:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Color: {self.color}"

class Coloreado:
    def como_colorear(self):
        raise NotImplementedError

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado - {super().__str__()}, Lado: {self.lado}"
