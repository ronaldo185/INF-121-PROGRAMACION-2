class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_salario_mensual(self):
        return 0.0

    def __str__(self):
        return f"Nombre: {self.nombre}"


class EmpleadoTH(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_salario_mensual(self):
        return self.horas_trabajadas * self.tarifa_hora

    def __str__(self):
        return (f"{super().__str__()}, Horas Trabajadas: {self.horas_trabajadas}, "
                f"Tarifa por Hora: {self.tarifa_hora}, "
                f"Salario Mensual: {self.calcular_salario_mensual()}")
