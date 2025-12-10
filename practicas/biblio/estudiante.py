class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Codigo: {self.codigo}")
