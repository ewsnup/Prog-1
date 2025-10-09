"""
Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo.
Deberá retornar un valor booleano indicando lo sucedido.
"""

def es_palindromo(cadena: str) -> bool:

    return cadena == cadena[::-1]

print(es_palindromo("reconocer"))     # True
print(es_palindromo("python"))        # False
