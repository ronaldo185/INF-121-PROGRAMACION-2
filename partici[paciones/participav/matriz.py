class Matriz:
    def __init__(self, mat):
        self.mat = mat
        self.n = len(mat)
        self.m = len(mat[0]) if mat else 0

    def __add__(self, otro):
        if self.n != otro.n or self.m != otro.m:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumar.")
        
        resultado = []
        for i in range(self.n):
            fila = []
            for j in range(self.m):
                fila.append(self.mat[i][j] + otro.mat[i][j])
            resultado.append(fila)
        return Matriz(resultado)

    def __mul__(self, otro):
        if self.m != otro.n:
            raise ValueError("Número de columnas de la primera matriz debe ser igual al número de filas de la segunda.")
        
        resultado = []
        for i in range(self.n):
            fila = []
            for j in range(otro.m):
                suma = 0
                for k in range(self.m):
                    suma += self.mat[i][k] * otro.mat[k][j]
                fila.append(suma)
            resultado.append(fila)
        return Matriz(resultado)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, fila)) for fila in self.mat])


A = Matriz([[1, 2], [3, 4]])
B = Matriz([[5, 6], [7, 8]])

C = A + B
print("A + B =")
print(C)

D = A * B
print("\nA * B =")
print(D)
