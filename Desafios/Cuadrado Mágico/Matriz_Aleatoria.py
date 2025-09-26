import random

def generar_matriz_aleatoria(n) -> list:
    """Generar matriz aleatoria"""
    # Crear matriz vacía
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila = fila + [0]
        matriz = matriz + [fila]
    
    # Crear lista de números disponibles
    numeros_disponibles = []
    for num in range(1, n*n + 1):
        numeros_disponibles = numeros_disponibles + [num]
    
    # Mezclar números
    for i in range(len(numeros_disponibles)):
        pos_aleatoria = random.randint(0, len(numeros_disponibles)-1)
        # Intercambiar
        temp = numeros_disponibles[i]
        numeros_disponibles[i] = numeros_disponibles[pos_aleatoria]
        numeros_disponibles[pos_aleatoria] = temp
    
    # Llenar matriz
    indice = 0
    for i in range(n):
        for j in range(n):
            matriz[i][j] = numeros_disponibles[indice]
            indice = indice + 1
    
    return matriz