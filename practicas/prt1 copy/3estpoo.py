# 3 Estadsticas: calcular el promedio y la desviacion estandar.
# usando programacion orientada a objetos
import math

class Estadistica:
    def __init__(self, valores):
        self.val = valores

    def promedio(self):
        return sum(self.val) / len(self.val)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom) ** 2 for x in self.val)
        return math.sqrt(suma / (len(self.val) - 1))

entrada = input("Ingrese 10 números: ")
numeros = list(map(float, entrada.split()))
if len(numeros) != 10:
    print("solo 10 números.")
else:
    estad = Estadistica(numeros)
    print(f"El promedio es {estad.promedio():.2f}")
    print(f"La desviación estándar es {estad.desviacion():.5f}")