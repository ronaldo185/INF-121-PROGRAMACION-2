import tkinter as tk
from tkinter import messagebox, simpledialog

from biblioteca import Biblioteca
from autor import Autor
from libro import Libro
from pagina import Pagina
from estudiante import Estudiante

import json
from datetime import datetime

ARCHIVO = "biblioteca.json"

def guardar_biblioteca(biblio: Biblioteca):
    data = {
        "nombre": biblio.nombre,
        "horario": {
            "dias_apertura": biblio.horario.dias_apertura,
            "hora_apertura": biblio.horario.hora_apertura,
            "hora_cierre": biblio.horario.hora_cierre
        },
        "autores": [
            {"nombre": a.nombre, "nacionalidad": a.nacionalidad}
            for a in biblio.autores
        ],
        "libros": [
            {
                "titulo": l.titulo,
                "isbn": l.isbn,
                "paginas": [
                    {"numero": p.numero, "contenido": p.contenido}
                    for p in l.paginas
                ]
            }
            for l in biblio.libros
        ],
        "prestamos": [
            {
                "estudiante": {
                    "codigo": p.estudiante.codigo,
                    "nombre": p.estudiante.nombre
                },
                "libro": p.libro.titulo,
                "fecha_prestamo": p.fecha_prestamo.isoformat(),
                "fecha_devolucion": p.fecha_devolucion.isoformat()
            }
            for p in biblio.prestamos
        ]
    }

    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

    print("✔ Biblioteca guardada correctamente.")


def cargar_biblioteca():
    try:
        with open(ARCHIVO, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No existe biblioteca.json, se creará una nueva.")
        return None

    biblio = Biblioteca(
        data["nombre"],
        data["horario"]["dias_apertura"],
        data["horario"]["hora_apertura"],
        data["horario"]["hora_cierre"]
    )

    # Autores
    for a in data["autores"]:
        biblio.agregar_autor(Autor(a["nombre"], a["nacionalidad"]))

    # Libros
    for l in data["libros"]:
        paginas = [Pagina(p["numero"], p["contenido"]) for p in l["paginas"]]
        libro = Libro.desde_paginas(l["titulo"], l["isbn"], paginas)
        biblio.agregar_libro(libro)

    # Préstamos
    for pr in data["prestamos"]:
        est = Estudiante(pr["estudiante"]["codigo"], pr["estudiante"]["nombre"])
        libro = next((x for x in biblio.libros if x.titulo == pr["libro"]), None)
        if libro:
            prestamo = prestamo(est, libro)
            biblio.prestamos.append(prestamo)

    print("✔ Biblioteca cargada desde JSON")
    return biblio




class App:
    def __init__(self, root):
        self.root = root
        root.title("Sistema de Biblioteca")

        # Cargar biblioteca
        self.biblio = cargar_biblioteca()
        if self.biblio is None:
            self.biblio = Biblioteca("Biblioteca UMSA", "Lunes a Viernes", "08:00", "18:00")

        # Botones
        tk.Button(root, text="Agregar Autor", width=30, command=self.agregar_autor).pack(pady=4)
        tk.Button(root, text="Agregar Libro", width=30, command=self.agregar_libro).pack(pady=4)
        tk.Button(root, text="Registrar Préstamo", width=30, command=self.prestar_libro).pack(pady=4)
        tk.Button(root, text="Mostrar Estado", width=30, command=self.mostrar_estado).pack(pady=4)
        tk.Button(root, text="Guardar Biblioteca", width=30, command=self.guardar).pack(pady=4)
        tk.Button(root, text="Salir", width=30, command=root.quit).pack(pady=4)

    # --------------------------
    # Funciones del menú
    # --------------------------

    def agregar_autor(self):
        nombre = simpledialog.askstring("Autor", "Nombre del autor:")
        nac = simpledialog.askstring("Autor", "Nacionalidad:")
        if nombre and nac:
            self.biblio.agregar_autor(Autor(nombre, nac))
            messagebox.showinfo("OK", "Autor agregado.")

    def agregar_libro(self):
        titulo = simpledialog.askstring("Libro", "Título del libro:")
        isbn = simpledialog.askstring("Libro", "ISBN:")
        if not titulo or not isbn:
            return

        libro = Libro(titulo, isbn, [])

        self.biblio.agregar_libro(libro)
        messagebox.showinfo("OK", "Libro agregado.")


    def prestar_libro(self):
        codigo = simpledialog.askstring("Estudiante", "Código:")
        nombre = simpledialog.askstring("Estudiante", "Nombre:")
        est = Estudiante(codigo, nombre)

        titulos = [l.titulo for l in self.biblio.libros]
        lista = "\n".join(f"{i+1}. {t}" for i, t in enumerate(titulos))

        idx = simpledialog.askinteger("Elegir libro", f"Seleccione un libro:\n{lista}") - 1
        if 0 <= idx < len(self.biblio.libros):
            self.biblio.prestar_libro(est, self.biblio.libros[idx])
            messagebox.showinfo("OK", "Préstamo registrado.")
        else:
            messagebox.showerror("Error", "Selección inválida.")

    def mostrar_estado(self):
        texto = f"Biblioteca: {self.biblio.nombre}\n\n"
        texto += "Autores:\n" + "\n".join(a.nombre for a in self.biblio.autores) + "\n\n"
        texto += "Libros:\n" + "\n".join(l.titulo for l in self.biblio.libros) + "\n\n"
        texto += f"Préstamos activos: {len(self.biblio.prestamos)}"

        messagebox.showinfo("Estado de Biblioteca", texto)

    def guardar(self):
        guardar_biblioteca(self.biblio)
        messagebox.showinfo("Guardado", "Biblioteca guardada correctamente.")



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
