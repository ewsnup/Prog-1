def es_entero(cadena: str) -> bool:
    """
    Valida si una cadena representa un número entero
    """
    if not cadena:
        return False
    
    inicio = 1 if cadena[0] == '-' else 0
    
    for i in range(inicio, len(cadena)):
        caracter = cadena[i]
        es_digito = False
        for digito in "0123456789":
            if caracter == digito:
                es_digito = True
                break
        if not es_digito:
            return False
    
    return cadena != "-" and cadena != ""

def convertir_a_entero(cadena: str) -> int:
    """
    Convierte una cadena a entero manualmente
    """
    valor = 0
    signo = 1
    inicio = 0
    
    if cadena[0] == '-':
        signo = -1
        inicio = 1
    
    for i in range(inicio, len(cadena)):
        digito = cadena[i]
        for j in range(10):
            if digito == str(j):
                valor = valor * 10 + j
                break
    
    return valor * signo

def es_par(numero: int) -> bool:
    """
    Determina si un número es par sin usar operador módulo
    """
    if numero < 0:
        numero = -numero
    
    while numero >= 2:
        numero = numero - 2
    
    return numero == 0