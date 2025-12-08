import json
import os
from medico import Medico
from consulta import Consulta

class Consultorio:
    def __init__(self):
        self.medicos = load_json("prubas/medicos.json")
        self.consultas = load_json("prubas/consultas.json")

    def guardar(self):
        save_json("prubas/medicos.json", self.medicos)
        save_json("prubas/consultas.json", self.consultas)

    def agregar_medico(self, medico):
        self.medicos.append(medico.to_dict())
        self.guardar()

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta.to_dict())
        self.guardar()

    def eliminar_medico(self, nombre, apellido):
        medicos_filtrados = []
        ids_eliminar = []

        for m in self.medicos:
            if m["nombremed"] == nombre and m["apellidomed"] == apellido:
                ids_eliminar.append(m["idmed"])
            else:
                medicos_filtrados.append(m)

        self.medicos = medicos_filtrados

        consultas_filtradas = [
            c for c in self.consultas if c["idmed"] not in ids_eliminar
        ]

        self.consultas = consultas_filtradas
        self.guardar()

    def corregifechas(self, otrodia):
        for c in self.consultas:
            if c["dia"] == 25 and c["mes"].lower() == "diciembre":
                c["dia"] = otrodia
            if c["dia"] == 1 and c["mes"].lower() == "enero":
                c["dia"] = otrodia
        self.guardar()

    def cumple(self, dia, mes):
        pacientes = [
            c for c in self.consultas
            if c["dia"] == dia and c["mes"].lower() == mes.lower()
        ]
        return pacientes


def load_json(nombre):
    if not os.path.exists(nombre):
        return []
    with open(nombre, "r") as f:
        return json.load(f)

def save_json(nombre, data):
    with open(nombre, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    consultorio = Consultorio()

    m1 = Medico(1, "Juan", "Perez", 10)
    m2 = Medico(2, "Maria", "Lopez", 8)
    m3 = Medico(3, "Carlos", "Gomez", 15)

    consultorio.agregar_medico(m1)
    consultorio.agregar_medico(m2)
    consultorio.agregar_medico(m3)

    consultas = [
        Consulta(112, "Luis", "Rios", 1, 25, "diciembre", 2024),
        Consulta(113, "Sofia", "Mendez", 1, 1, "enero", 2024),   

        Consulta(116, "Rocio", "Morales", 2, 7, "junio", 2024),  

        Consulta(117, "Pedro", "Suarez", 3, 1, "enero", 2024),    
        Consulta(118, "Miguel", "Garcia", 3, 3, "marzo", 2024),
    ]

    for c in consultas:
        consultorio.agregar_consulta(c)

    consultorio.eliminar_medico("Maria", "Lopez")

    consultorio.corregifechas(otrodia=26)

    print("json actualizado")

    pacientes_cumple = consultorio.cumple(7, "junio")
    if pacientes_cumple:
        print("Pacientes atendidos el 7 de junio:")
        for c in pacientes_cumple:
            print(f"Paciente: {c['nombrepaciente']} {c['apellidopaciente']}, Fecha: {c['dia']} de {c['mes']} de {c['anio']}")
    else:
        print("No hubo pacientes atendidos el 7 de junio.")
    