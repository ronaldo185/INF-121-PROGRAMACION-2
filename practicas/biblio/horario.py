class Horario:
    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrar_horario(self):
        print(f"Horario: {self.dias_apertura} de {self.hora_apertura} a {self.hora_cierre}")
