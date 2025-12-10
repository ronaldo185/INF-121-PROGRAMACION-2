# 3 Estadsticas: calcular el promedio y la desviacion estandar.
# usando programacion estructurada - modular
import math

def promedio(valores):
    return sum(valores) / len(valores)

def desviacion(valores):
    prom = promedio(valores)
    suma = sum((x - prom) ** 2 for x in valores)
    return math.sqrt(suma / (len(valores) - 1))

entrada = input("Ingrese 10 números separados por espacio: ")
numeros = list(map(float, entrada.split()))
if len(numeros) != 10:
    print("solo 10 números")
else:
    print(f"El promedio es {promedio(numeros):.2f}")
    print(f"La desviación estándar es {desviacion(numeros):.5f}")