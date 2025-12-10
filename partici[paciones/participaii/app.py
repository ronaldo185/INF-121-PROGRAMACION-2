class Lampara:
    def __init__(self, color_luz, brillo):
        self.estado = False
        self.color_luz = color_luz
        self.brillo = brillo

    def encender(self):
        self.estado = True
        print("La lámpara está encendida.")

    def apagar(self):
        self.estado = False
        print("La lámpara está apagada.")

    def ajustar_brillo(self, nuevo_brillo):
        self.brillo = nuevo_brillo
        print(f"Brillo ajustado a {self.brillo}")

    def __str__(self):
        return f"Lámpara(color_luz={self.color_luz}, brillo={self.brillo}, estado={'encendida' if self.estado else 'apagada'})"

