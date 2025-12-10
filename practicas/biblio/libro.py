from biblio.pagina import Pagina

class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [] 

    def agregar_pagina(self, pagina):
        self.paginas.append(pagina)

    def leer(self):
        print(f"Leyendo libro: {self.titulo}")
        for pagina in self.paginas:
            pagina.mostrar_pagina()
