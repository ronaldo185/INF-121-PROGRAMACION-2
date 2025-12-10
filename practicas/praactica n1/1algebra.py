# 1 Algebra: ecuacion lineal

# Definición de la clase para resolver ecuaciones lineales de dos variables
class EcuacionLineal:
    
    # Constructor que recibe los coeficientes de las ecuaciones
    def __init__(self, a, b, c, d, e, f):
        self.a = a  # Coeficiente de x en la primera ecuación
        self.b = b  # Coeficiente de y en la primera ecuación
        self.c = c  # Coeficiente de x en la segunda ecuación
        self.d = d  # Coeficiente de y en la segunda ecuación
        self.e = e  # Término independiente de la primera ecuación
        self.f = f  # Término independiente de la segunda ecuación

    # Método para verificar si el sistema tiene solución única
    def tieneSolucion(self):
        return (self.a * self.d - self.b * self.c) != 0  # Determinante distinto de cero

    # Método para calcular el valor de x
    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)  # Fórmula de Cramer para x

    # Método para calcular el valor de y
    def getY(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)  # Fórmula de Cramer para y

# Solicita al usuario que ingrese los valores de los coeficientes y términos independientes
entrada = input("Ingrese a, b, c, d, e, f : ")

# Convierte la entrada en una lista de números flotantes
valores = list(map(float, entrada.split()))

# Asigna cada valor a su respectiva variable
a, b, c, d, e, f = valores

# Crea una instancia de la clase EcuacionLineal con los valores ingresados
ecuacion = EcuacionLineal(a, b, c, d, e, f)

# Verifica si el sistema tiene solución y muestra los resultados
if ecuacion.tieneSolucion():
    print(f"x = {ecuacion.getX()}, y = {ecuacion.getY()}")  # Imprime los valores de x e y
else:
    print("La ecuación no tiene solución")  # Informa que no hay solución
