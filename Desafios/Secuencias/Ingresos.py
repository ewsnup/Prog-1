from Validaciones import es_entero, convertir_a_entero
from Matriz import crear_matriz

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int:
    """
    Pide un número entero por consola con validaciones
    """
    intentos = 0
    
    while intentos <= reintentos:
        print(mensaje)
        entrada = input()
        
        if not es_entero(entrada):
            print(mensaje_error)
            intentos += 1
            continue
        
        valor = convertir_a_entero(entrada)
        
        if minimo <= valor <= maximo:
            return valor
        else:
            print(mensaje_error)
            intentos += 1
    
    return minimo

def ingresar_matriz_manual(filas: int, columnas: int) -> list:
    """
    Permite al usuario ingresar una matriz manualmente
    """
    matriz = crear_matriz(filas, columnas)
    print(f"\nIngrese los valores para la matriz {filas}x{columnas}:")
    
    for i in range(filas):
        for j in range(columnas):
            mensaje = f"Fila {i+1}, Columna {j+1}: "
            numero = get_int(mensaje, "Error: ingrese un número entero válido", -1000, 1000, 3)
            matriz[i][j] = numero
    
    return matriz