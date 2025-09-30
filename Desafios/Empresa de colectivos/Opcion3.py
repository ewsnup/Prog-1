lineas = 3
coches_por_linea = 5


def calcular_recaudacion_por_linea(matriz_recaudaciones):
    print("\n--- RECAUDACIÓN POR LÍNEA ---")
    
    i = 0
    while i < lineas:
        total_linea = 0.0
        j = 0
        while j < coches_por_linea:
            total_linea = total_linea + matriz_recaudaciones[i][j]
            j = j + 1
        print("Línea " + str(i+1) + ": $" + f"{total_linea:.2f}")
        i = i + 1