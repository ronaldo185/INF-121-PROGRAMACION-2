
class Consulta:
    def __init__(self, ci, nombrepac, apellidopac, idmed, dia, mes, anio):
        self.ci = ci
        self.nombrepaciente = nombrepac
        self.apellidopaciente = apellidopac
        self.idmed = idmed
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def to_dict(self):
        return {
            "ci": self.ci,
            "nombrepaciente": self.nombrepaciente,
            "apellidopaciente": self.apellidopaciente,
            "idmed": self.idmed,
            "dia": self.dia,
            "mes": self.mes,
            "anio": self.anio
        }
