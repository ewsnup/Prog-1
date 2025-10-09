"""
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente).
La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ejemplo, si la cadena ingresada es “murcielaguito”, la salada por pantalla deberá ser: (“a”: 1; 
                                                                                            “e”: 1;    
                                                                                            “i”: 2; 
                                                                                            “o”: 1; 
                                                                                            “u”: 2)

"""

def cantidad_de_vocales(cadena: str) -> list:

    letra_a = 0
    letra_e = 0
    letra_i = 0
    letra_o = 0
    letra_u = 0


    for caracter in cadena:
        if caracter == "a":
            letra_a += 1
        elif caracter == "e":
            letra_e += 1
        elif caracter == "i":
            letra_i += 1
        elif caracter == "o":
            letra_o += 1
        elif caracter == "u":
            letra_u += 1

    matriz = [
        ["a", letra_a],
        ["e", letra_e],
        ["i", letra_i],
        ["o", letra_o],
        ["u", letra_u]
    ]

    return matriz

cadena = input("Ingrese un string: ")
resultado = cantidad_de_vocales(cadena)

print("La salida por pantalla será:")
for vocal, cantidad in resultado:
    print(f'"{vocal}": {cantidad}')