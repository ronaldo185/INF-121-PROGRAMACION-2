# 2 Algebra: Ecuaciones Cuadraticas
import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        return (-self.b + math.sqrt(d)) / (2*self.a)

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        return (-self.b - math.sqrt(d)) / (2*self.a)

entrada = input("Ingrese a, b, c: ")
a, b, c = map(float, entrada.split())
ecuacion = EcuacionCuadratica(a, b, c)
d = ecuacion.getDiscriminante()
if d > 0:
    print(f"La ecuación tiene dos raíces {ecuacion.getRaiz1()} y {ecuacion.getRaiz2()}")
elif d == 0:
    print(f"La ecuación tiene una raíz {ecuacion.getRaiz1()}")
else:
    print("La ecuación no tiene raíces reales")