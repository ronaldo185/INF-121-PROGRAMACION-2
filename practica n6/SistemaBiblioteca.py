from biblioteca import Biblioteca
from autor import Autor
from libro import Libro
from pagina import Pagina
from estudiante import Estudiante


if __name__ == '__main__':
    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca UMSA", "Lunes a Viernes", "08:00", "18:00")

    # Crear autores
    autor1 = Autor("Gabriel Garcia Marquez", "Colombiano")
    autor2 = Autor("Isabel Allende", "Chilena")
    biblioteca.agregar_autor(autor1)
    biblioteca.agregar_autor(autor2)


    # Crear libros con páginas (composición Libro-Pagina)
    libro1 = Libro("Cien Años de Soledad", "ISBN001", [])
    libro1.agregar_pagina(Pagina(1, "Capítulo 1..."))
    libro1.agregar_pagina(Pagina(2, "Capítulo 2..."))


    libro2 = Libro("La Casa de los Espíritus", "ISBN002", [Pagina(1, "Capítulo 1...")])


    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)


    # Crear estudiante
    estudiante = Estudiante("S001", "Juan Perez")


    # Prestar libro
    biblioteca.prestar_libro(estudiante, libro1)


    # Mostrar estado
    biblioteca.mostrar_estado()


    # Cerrar biblioteca
    biblioteca.cerrar_biblioteca()