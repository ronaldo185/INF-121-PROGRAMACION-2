from entero import entero

num1 = entero(7)
num2 = entero(10)
# métodos de instancia
print("num1 =", num1.getValor())
print("¿num1 es par?", num1.esPar())
print("¿num1 es impar?", num1.esImpar())
print("¿num1 es primo?", num1.esPrimo())
print("\nnum2 =", num2.getValor())
print("¿num2 es par?", num2.esPar())
print("¿num2 es impar?", num2.esImpar())
print("¿num2 es primo?", num2.esPrimo())
# Probar equals
print("\n¿num1 == 7?", num1.equals(7))
print("¿num1 == num2?", num1.equals(num2))
# métodos estáticos
print("\n¿15 es par?", entero.esPar_int(15))
print("¿15 es impar?", entero.esImpar_int(15))
print("¿15 es primo?", entero.esPrimo_int(15))
# métodos estáticos con objeto entero
print("\n¿num1 es par? (clase)", entero.esPar_obj(num1))
print("¿num1 es primo? (clase)", entero.esPrimo_obj(num1))
#
print("\nparseInt(['1','2','3']) =", entero.parseInt_chars(['1', '2', '3']))
print("parseIntString('456') =", entero.parseInt_string("456"))