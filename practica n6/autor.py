class Autor:
    def __init__(self, nombre: str, nacionalidad: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad


    def mostrar_info(self) -> None:
        print(f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}")

    def __str__(self) -> str:
        return f"{self.nombre} ({self.nacionalidad})"