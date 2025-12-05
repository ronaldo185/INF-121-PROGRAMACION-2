class Horario:

    def __init__(self, dias_apertura: str, hora_apertura: str, hora_cierre: str):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre


    def mostrar_horario(self) -> None:
        print(f"Horario: {self.dias_apertura} de {self.hora_apertura} a {self.hora_cierre}")

    def __str__(self) -> str:
        return f"{self.dias_apertura} {self.hora_apertura}-{self.hora_cierre}"