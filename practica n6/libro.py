from typing import List
from pagina import Pagina


class Libro:
    
    def __init__(self, titulo: str, isbn: str, paginas: List[Pagina] = None):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas: List[Pagina] = paginas or []

    @classmethod
    def desde_paginas(cls, titulo: str, isbn: str, paginas: List[Pagina]):
        return cls(titulo, isbn, paginas)


    def agregar_pagina(self, pagina: Pagina) -> None:
        self.paginas.append(pagina)

    def leer(self) -> None:
        print(f"\nLeyendo libro: {self.titulo}")
        for p in self.paginas:
            p.mostrar_pagina()


    def get_titulo(self) -> str:
        return self.titulo

    def __str__(self) -> str:
        return f"{self.titulo} (ISBN: {self.isbn})"