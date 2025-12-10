class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}")
