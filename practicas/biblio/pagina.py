class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrar_pagina(self):
        print(f"Pagina {self.numero}: {self.contenido}")
