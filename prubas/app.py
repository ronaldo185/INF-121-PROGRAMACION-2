
from consultorio import Consultorio
from medico import Medico
from consulta import Consulta


if __name__ == "__main__":
    consultorio = Consultorio()

    m1 = Medico(1, "Juan", "Perez", 10)
    m2 = Medico(2, "Maria", "Lopez", 8)
    m3 = Medico(3, "Carlos", "Gomez", 15)

    consultorio.agregar_medico(m1)
    consultorio.agregar_medico(m2)
    consultorio.agregar_medico(m3)

    consultas = [
        Consulta(111, "Ana", "Diaz", 1, 10, "junio", 2024),
        Consulta(112, "Luis", "Rios", 1, 25, "diciembre", 2024),  # navidad
        Consulta(113, "Sofia", "Mendez", 1, 1, "enero", 2024),    # año nuevo

        Consulta(114, "Carlos", "Alba", 2, 7, "abril", 2024),
        Consulta(115, "Jose", "Calderon", 2, 22, "mayo", 2024),
        Consulta(116, "Rocio", "Morales", 2, 25, "diciembre", 2024),  # navidad

        Consulta(117, "Pedro", "Suarez", 3, 1, "enero", 2024),    # año nuevo
        Consulta(118, "Miguel", "Garcia", 3, 3, "marzo", 2024),
        Consulta(119, "Laura", "Ortega", 3, 15, "julio", 2024),
    ]

    for c in consultas:
        consultorio.agregar_consulta(c)
    consultorio.eliminar_medico("Maria", "Lopez")

    consultorio.corregir_fechas_especiales(nuevo_dia=26)

    print("json actualizado")
