import random

def crear_matriz(filas: int, columnas: int) -> list:
    """
    Crea una matriz vacía del tamaño especificado
    """
    matriz = [None] * filas
    for i in range(filas):
        matriz[i] = [0] * columnas
    return matriz

def generar_matriz_aleatoria(filas: int, columnas: int) -> list:
    """
    Genera una matriz con valores aleatorios
    """
    matriz = crear_matriz(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = random.randint(-50, 50)
    return matriz

def mostrar_matriz(matriz: list):
    """
    Muestra la matriz en formato legible
    """
    print("\nMatriz:")
    for i in range(len(matriz)):
        fila_str = ""
        for j in range(len(matriz[i])):
            fila_str = fila_str + str(matriz[i][j]) + "\t"
        print(fila_str)

           