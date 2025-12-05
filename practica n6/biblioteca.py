import json
from libro import Libro
from autor import Autor
from prestamo import Prestamo
from estudiante import Estudiante

class Biblioteca:
    class Horario:
        def __init__(self, dias_apertura: str, hora_apertura: str, hora_cierre: str):
            self.dias_apertura = dias_apertura
            self.hora_apertura = hora_apertura
            self.hora_cierre = hora_cierre

        def mostrar_horario(self):
            print(f"Horario: {self.dias_apertura} de {self.hora_apertura} a {self.hora_cierre}")

        def __str__(self):
            return f"{self.dias_apertura} {self.hora_apertura}-{self.hora_cierre}"

    def __init__(self, nombre: str, dias_apertura: str, hora_apertura: str, hora_cierre: str):
        self.nombre = nombre
        self.horario = Biblioteca.Horario(dias_apertura, hora_apertura, hora_cierre)  # composición
        self.libros: list[Libro] = [] 
        self.autores: list[Autor] = []     
        self.prestamos: list[Prestamo] = []  

    # Métodos para agregar libros
    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    # Métodos para agregar autores
    def agregar_autor(self, autor: Autor):
        self.autores.append(autor)

    # Método para prestar libros
    def prestar_libro(self, estudiante: Estudiante, libro: Libro):
        p = Prestamo(estudiante, libro)
        self.prestamos.append(p)
        print(f"Libro prestado exitosamente: {libro.get_titulo()}")

    # Método para mostrar el estado de la biblioteca
    def mostrar_estado(self):
        print(f"\n--- Biblioteca: {self.nombre} ---")
        self.horario.mostrar_horario()

        print("\nLibros disponibles:")
        for l in self.libros:
            print(f"- {l.get_titulo()}")

        print("\nAutores registrados:")
        for a in self.autores:
            a.mostrar_info()

        print("\nPrestamos activos:")
        for p in self.prestamos:
            p.mostrar_info()

    # Método para cerrar la biblioteca
    def cerrar_biblioteca(self):
        self.prestamos.clear()
        print(f"\nLa biblioteca {self.nombre} cerrado")
