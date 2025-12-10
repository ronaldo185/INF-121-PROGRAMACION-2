from biblioteca import Biblioteca
from libro import Libro
from autor import Autor
from estudiante import Estudiante
from pagina import Pagina
from horario import Horario

# Crear horario
horario = Horario("Lunes a Viernes", "08:00", "18:00")

# Crear biblioteca
biblioteca = Biblioteca("Biblioteca UMSA", horario)

# Crear autores
autor1 = Autor("Gabriel Garcia Marquez", "Colombiano")
autor2 = Autor("Isabel Allende", "Chilena")
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

# Crear libros
libro1 = Libro("Cien Años de Soledad", "ISBN001")
libro1.agregar_pagina(Pagina(1, "Capítulo 1..."))
libro1.agregar_pagina(Pagina(2, "Capítulo 2..."))

libro2 = Libro("La Casa de los Espíritus", "ISBN002")
libro2.agregar_pagina(Pagina(1, "Capítulo 1..."))

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
