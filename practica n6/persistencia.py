import json

def guardar_biblioteca(biblio, archivo="biblioteca.json"):
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
        ]
    }

    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)

    print("Biblioteca guardada correctamente. (al menos eso creo)")


def cargar_biblioteca(Biblioteca, Autor, Libro, Pagina, archivo="biblioteca.json"):
    try:
        with open(archivo, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("⚠ No existe archivo previo... así que tocará empezar de cero.")
        return None

    b = Biblioteca(
        data["nombre"],
        data["horario"]["dias_apertura"],
        data["horario"]["hora_apertura"],
        data["horario"]["hora_cierre"]
    )

    for a in data["autores"]:
        b.agregar_autor(Autor(a["nombre"], a["nacionalidad"]))

    for l in data["libros"]:
        libro = Libro(l["titulo"], l["isbn"], [])

        for p in l["paginas"]:
            libro.agregar_pagina(Pagina(p["numero"], p["contenido"]))

        b.agregar_libro(libro)

    print("Biblioteca cargada desde archivo. (sobrevivió!)")
    return b
