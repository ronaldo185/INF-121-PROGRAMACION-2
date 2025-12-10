from horario import Horario
from prestamo import Prestamo

class Biblioteca:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario  
        self.libros = []        
        self.autores = []       
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def prestar_libro(self, estudiante, libro):
        from prestamo import Prestamo
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"Libro prestado exitosamente: {libro.titulo}")

    def mostrar_estado(self):
        print(f"\n--- Biblioteca: {self.nombre} ---")
        self.horario.mostrar_horario()

        print("\nLibros disponibles:")
        for libro in self.libros:
            print(f"- {libro.titulo}")

        print("\nAutores registrados:")
        for autor in self.autores:
            autor.mostrar_info()

        print("\nPrestamos activos:")
        for prestamo in self.prestamos:
            prestamo.mostrar_info()
            print()

    def cerrar_biblioteca(self):
        self.prestamos.clear()
        print(f"La biblioteca {self.nombre} ha cerrado. Todos los prestamos han sido eliminados.")
