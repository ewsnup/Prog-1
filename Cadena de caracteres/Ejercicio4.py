"""
Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.
"""

def suprimir_repetidos_consecutivos(cadena: str) -> str:

    resultado = cadena[0] 
    
    for i in range(1, len(cadena)):
        if cadena[i] != cadena[i - 1]:
            resultado += cadena[i]
    
    return resultado

print(suprimir_repetidos_consecutivos("Mississippi"))