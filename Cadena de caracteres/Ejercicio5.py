"""
Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.

Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
"""

def suprimir_vocales(cadena: str) -> str:

    vocales = ["a", "e", "i", "o", "u"]
    resultado = ""
    
    for caracter in cadena:
        if caracter not in vocales: 
            resultado += caracter
    
    return resultado

print(suprimir_vocales("Mississippi"))

