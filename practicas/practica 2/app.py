import math

class AlgebraVectorial:

    def __init__(self, a=None, b=None):
        if a is None:
            self.a = [0, 0, 0]
        else:
            self.a = a

        if b is None:
            self.b = [0, 0, 0]
        else:
            self.b = b


    def norma(self, v):
        return math.sqrt(sum(x*x for x in v))

    def suma(self, a, b):
        return [a[i] + b[i] for i in range(len(a))]

    def resta(self, a, b):
        return [a[i] - b[i] for i in range(len(a))]

    def dot(self, a, b):
        return sum(a[i] * b[i] for i in range(len(a)))

    def cross(self, a, b):
        return [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ]

    def perpendicular(self, metodo=1):
        a, b = self.a, self.b

        if metodo == 1:
            return abs(self.norma(self.suma(a, b)) - self.norma(self.resta(a, b))) < 1e-9

        if metodo == 2:
            return abs(self.norma(self.resta(a, b)) - self.norma(self.resta(b, a))) < 1e-9

        if metodo == 3:
            return abs(self.dot(a, b)) < 1e-9

        if metodo == 4:
            lhs = self.norma(self.suma(a, b))**2
            rhs = self.norma(a)**2 + self.norma(b)**2
            return abs(lhs - rhs) < 1e-9



    def paralela(self, metodo=1):
        a, b = self.a, self.b

        if metodo == 1:

            try:
                r_vals = []
                for i in range(len(a)):
                    if b[i] != 0:
                        r_vals.append(a[i] / b[i])
                return len(set([round(r, 6) for r in r_vals])) == 1
            except:
                return False

        if metodo == 2:

            return self.cross(a, b) == [0, 0, 0]



    def proyeccion(self):
        a, b = self.a, self.b
        factor = self.dot(a, b) / (self.norma(b)**2)
        return [factor * bi for bi in b]


    def componente(self):
        a, b = self.a, self.b
        return self.dot(a, b) / self.norma(b)

    def __str__(self):
        return f"a={self.a}, b={self.b}"


v = AlgebraVectorial([2, 1, 0], [4, 2, 0])

print("Perpendicular (método 3 dot=0):", v.perpendicular(3))
print("Paralela (método 2 cross=0):", v.paralela(2))
print("Proyección de a sobre b:", v.proyeccion())
print("Componente de a en b:", v.componente())
