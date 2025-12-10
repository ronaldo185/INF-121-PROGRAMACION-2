# 2 Algebra: Ecuaciones Cuadraticas
import math  # Importa el módulo math para funciones matemáticas como sqrt

class EcuacionCuadratica:  # Define una clase para representar una ecuación cuadrática
    def __init__(self, a, b, c):  # Constructor que recibe los coeficientes a, b y c
        self.a = a  # Guarda el coeficiente a
        self.b = b  # Guarda el coeficiente b
        self.c = c  # Guarda el coeficiente c

    def getDiscriminante(self):  # Método para calcular el discriminante
        return self.b**2 - 4*self.a*self.c  # Fórmula del discriminante: b^2 - 4ac

    def getRaiz1(self):  # Método para calcular la primera raíz
        d = self.getDiscriminante()  # Obtiene el discriminante
        if d < 0:  # Si el discriminante es negativo, no hay raíces reales
            return 0  # Retorna 0 si no hay raíz real
        return (-self.b + math.sqrt(d)) / (2*self.a)  # Fórmula de la primera raíz

    def getRaiz2(self):  # Método para calcular la segunda raíz
        d = self.getDiscriminante()  # Obtiene el discriminante
        if d < 0:  # Si el discriminante es negativo, no hay raíces reales
            return 0  # Retorna 0 si no hay raíz real
        return (-self.b - math.sqrt(d)) / (2*self.a)  # Fórmula de la segunda raíz

entrada = input("Ingrese a, b, c: ")  # Solicita al usuario los coeficientes separados por espacio
a, b, c = map(float, entrada.split())  # Convierte la entrada en tres números flotantes
ecuacion = EcuacionCuadratica(a, b, c)  # Crea una instancia de la clase con los coeficientes dados
d = ecuacion.getDiscriminante()  # Calcula el discriminante
if d > 0:  # Si el discriminante es positivo, hay dos raíces reales
    print(f"La ecuación tiene dos raíces {ecuacion.getRaiz1()} y {ecuacion.getRaiz2()}")  # Muestra ambas raíces
elif d == 0:  # Si el discriminante es cero, hay una raíz real doble
    print(f"La ecuación tiene una raíz {ecuacion.getRaiz1()}")  # Muestra la raíz doble
else:  # Si el discriminante es negativo, no hay raíces reales
    print("La ecuación no tiene raíces reales")  # Informa que no existen raíces reales