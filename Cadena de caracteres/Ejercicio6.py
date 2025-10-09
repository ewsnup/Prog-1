"""
Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.

"""

def contar_subcadena(cadena: str, subcadena: str) -> int:

    contador = 0
    longitud_sub = len(subcadena)
    
    for i in range(len(cadena) - longitud_sub + 1):
        if cadena[i:i + longitud_sub] == subcadena:
            contador += 1
    
    return contador

print(contar_subcadena("El pan del panadero", "pan"))