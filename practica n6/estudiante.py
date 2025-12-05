class Estudiante:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre


    def mostrar_info(self) -> None:
        print(f"Estudiante: {self.nombre}, Codigo: {self.codigo}")

    def __str__(self) -> str:
        return f"{self.nombre} [{self.codigo}]"