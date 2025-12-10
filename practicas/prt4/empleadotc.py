class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_salario_mensual(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def __str__(self):
        return f"Nombre: {self.nombre}"


class EmpleadoTC(Empleado):
    def __init__(self, nombre, salario_anual):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self):
        return self.salario_anual / 12

    def __str__(self):
        return (super().__str__() +
                f", Salario Anual: {self.salario_anual}, Salario Mensual: {self.calcular_salario_mensual()}")
