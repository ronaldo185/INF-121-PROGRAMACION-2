class Figura:
    def __init__(self, color):
        self._color = color

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def perimetro(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return f"Color: {self._color}"
