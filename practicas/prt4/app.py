class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def calcular_salario_mensual(self):
        raise NotImplementedError("Debe implementar este método en la subclase")


class EmpleadoTC(Empleado):
    def __init__(self, nombre, salario_anual):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self):
        return self.salario_anual / 12


class EmpleadoTH(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_salario_mensual(self):
        return self.horas * self.tarifa


def main():
    empleados = []

    print("=== Empleados Tiempo Completo ===")
    for i in range(3):
        nombre = input(f"Nombre del empleado {i + 1}: ")
        salario_anual = float(input("Salario anual: "))
        empleados.append(EmpleadoTC(nombre, salario_anual))

    print("\n=== Empleados Tiempo Horario ===")
    for i in range(2):
        nombre = input(f"Nombre del empleado {i + 1}: ")
        horas = float(input("Horas trabajadas en el mes: "))
        tarifa = float(input("Tarifa por hora: "))
        empleados.append(EmpleadoTH(nombre, horas, tarifa))

    print("\n=== Lista de Empleados ===")
    for e in empleados:
        print(f"{e.get_nombre()} - Salario Mensual: {e.calcular_salario_mensual():.2f}")


if __name__ == "__main__":
    main()
