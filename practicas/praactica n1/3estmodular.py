# 3 Estadsticas: calcular el promedio y la desviacion estandar.
# usando programacion estructurada - modular

import math  # Importa el módulo math para funciones matemáticas

def promedio(valores):
    # Calcula el promedio de una lista de valores
    return sum(valores) / len(valores)

def desviacion(valores):
    # Calcula la desviación estándar de una lista de valores
    prom = promedio(valores)  # Obtiene el promedio de los valores
    suma = sum((x - prom) ** 2 for x in valores)  # Suma de los cuadrados de las diferencias
    return math.sqrt(suma / (len(valores) - 1))  # Aplica la fórmula de desviación estándar

entrada = input("Ingrese 10 números separados por espacio: ")  # Solicita al usuario los números
numeros = list(map(float, entrada.split()))  # Convierte la entrada en una lista de números flotantes

if len(numeros) != 10:
    # Verifica que se hayan ingresado exactamente 10 números
    print("solo 10 números")
else:
    # Si hay 10 números, muestra el promedio y la desviación estándar
    print(f"El promedio es {promedio(numeros):.2f}")  # Imprime el promedio con 2 decimales
    print(f"La desviación estándar es {desviacion(numeros):.5f}")  # Imprime la desviación estándar con 5 decimales