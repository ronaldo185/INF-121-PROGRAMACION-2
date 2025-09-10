class entero:
    def __init__(self, valor):
        self.__valor = valor

    def getValor(self):
        return self.__valor

    # Métodos de instancia
    def esPar(self):
        return self.__valor % 2 == 0

    def esImpar(self):
        return self.__valor % 2 != 0

    def esPrimo(self):
        return entero.esPrimo_int(self.__valor)

    def equals(self, otro):
        if isinstance(otro, entero):
            return self.__valor == otro.getValor()
        elif isinstance(otro, int):
            return self.__valor == otro
        return False

    #Métodos estáticos
    def esPar_int(valor):
        return valor % 2 == 0

    def esImpar_int(valor):
        return valor % 2 != 0

    def esPrimo_int(valor):
        if valor <= 1:
            return False
        for i in range(2, int(valor**0.5) + 1):
            if valor % i == 0:
                return False
        return True

    def esPar_obj(obj):
        return obj.getValor() % 2 == 0

    def esImpar_obj(obj):
        return obj.getValor() % 2 != 0

    def esPrimo_obj(obj):
        return entero.esPrimo_int(obj.getValor())

    # parseInt de char[] -> int
    def parseInt_chars(chars):
        return int("".join(chars))

    # parseInt de String -> int
    def parseInt_string(cadena):
        return int(cadena)
