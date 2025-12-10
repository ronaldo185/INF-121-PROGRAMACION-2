# 3 Estadsticas: calcular el promedio y la desviacion estandar.
# usando programacion orientada a objetos

import math  # Importa el módulo math para funciones matemáticas

class Estadistica:  # Define una clase para cálculos estadísticos
    def __init__(self, valores):  # Constructor que recibe una lista de valores
        self.val = valores  # Guarda los valores en un atributo de la instancia

    def promedio(self):  # Método para calcular el promedio
        return sum(self.val) / len(self.val)  # Suma todos los valores y divide por la cantidad

    def desviacion(self):  # Método para calcular la desviación estándar
        prom = self.promedio()  # Calcula el promedio usando el método anterior
        suma = sum((x - prom) ** 2 for x in self.val)  # Suma los cuadrados de las diferencias respecto al promedio
        return math.sqrt(suma / (len(self.val) - 1))  # Calcula la raíz cuadrada de la varianza (desviación estándar)

entrada = input("Ingrese 10 números: ")  # Solicita al usuario que ingrese 10 números separados por espacio
numeros = list(map(float, entrada.split()))  # Convierte la entrada en una lista de números flotantes
if len(numeros) != 10:  # Verifica que se hayan ingresado exactamente 10 números
    print("solo 10 números.")  # Muestra un mensaje de error si no son 10
else:
    estad = Estadistica(numeros)  # Crea una instancia de la clase Estadistica con los números ingresados
    print(f"El promedio es {estad.promedio():.2f}")  # Imprime el promedio con 2 decimales
    print(f"La desviación estándar es {estad.desviacion():.5f}")  # Imprime la desviación estándar con 5 decimales