class Pagina:   
    def __init__(self, numero: int, contenido: str):
        self.numero = numero
        self.contenido = contenido


    def mostrar_pagina(self) -> None:
        print(f"Página {self.numero}: {self.contenido}")

    def __str__(self) -> str:
        return f"Página {self.numero}: {self.contenido[:30]}"