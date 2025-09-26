from Matriz_Aleatoria import generar_matriz_aleatoria

def generar_cuadrado_magico_valido(n) -> list:
    """Generar cuadrado mágico válido"""
    # Crear matriz vacía
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila = fila + [0]
        matriz = matriz + [fila]
    
    # Usar match case para diferentes métodos según n
    match n % 2:
        case 1:  # n impar - método siamese
            i, j = 0, n // 2
            for num in range(1, n*n + 1):
                matriz[i][j] = num
                
                # Movimiento diagonal arriba-derecha
                nuevo_i = (i - 1) % n
                nuevo_j = (j + 1) % n
                
                if matriz[nuevo_i][nuevo_j] != 0:
                    # Si la celda está ocupada, mover abajo
                    i = (i + 1) % n
                else:
                    i, j = nuevo_i, nuevo_j
        
        case 0:  # n par
            print("Nota: Para n par se genera matriz aleatoria")
            matriz_aleatoria = generar_matriz_aleatoria(n)
            return matriz_aleatoria
    
    return matriz