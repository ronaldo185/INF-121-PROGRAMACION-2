class Medico:
    def __init__(self, idmed, nombremed, apellidomed, aniosexp):
        self.idmed = idmed
        self.nombremed = nombremed
        self.apellidomed = apellidomed
        self.aniosexperiencia = aniosexp

    def to_dict(self):
        return {
            "idmed": self.idmed,
            "nombremed": self.nombremed,
            "apellidomed": self.apellidomed,
            "aniosexperiencia": self.aniosexperiencia
        }
