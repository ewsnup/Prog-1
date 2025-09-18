def es_positivo(numero: int) -> int:
    """
    Determina si un número es positivo
    """
    return numero > 0

def es_negativo(numero: int) -> int:
    """
    Determina si un número es negativo
    """
    return numero < 0

def es_par(numero: int) -> int:
    """
    Determina si un número es par
    """
    return numero % 2 == 0

def es_impar(numero: int) -> int:
    """
    Determina si un número es impar
    """
    return numero % 2 != 0

def contar_positivos_negativos(numeros: int) -> int:
    """
    Cuenta la cantidad de números positivos y negativos
    """
    positivos = 0
    negativos = 0
    
    for numero in numeros:
        if es_positivo(numero):
            positivos += 1
        elif es_negativo(numero):
            negativos += 1
    
    return positivos, negativos

def sumar_pares(numeros: int) -> int:
    """
    Calcula la suma de los números pares
    """
    suma = 0
    for numero in numeros:
        if es_par(numero):
            suma += numero
    return suma

def mayor_impar(numeros: int) -> int:
    """
    Encuentra el mayor número impar
    """
    mayor = None
    
    for numero in numeros:
        if es_impar(numero):
            if mayor is None or numero > mayor:
                mayor = numero
    
    return mayor