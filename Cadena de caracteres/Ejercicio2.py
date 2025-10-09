"""
Crear una función que reciba una cadena y un caracter.
La función deberá devolver el índice en el que se encuentre la primera ocurrencia de dicho caracter, o -1 en caso de que no esté.
"""

def devolver_indice_caracter(cadena: str, caracter: str) -> int:
    
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1

print(devolver_indice_caracter("murcielaguito", "u")) 
print(devolver_indice_caracter("murcielaguito", "x"))  