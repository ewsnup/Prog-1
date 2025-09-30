lineas = 3
coches_por_linea = 5

def calcular_recaudacion_total(matriz_recaudaciones):
    print("\n--- RECAUDACIÓN TOTAL ---")
    
    total_general = 0.0
    i = 0
    while i < lineas:
        j = 0
        while j < coches_por_linea:
            total_general = total_general + matriz_recaudaciones[i][j]
            j = j + 1
        i = i + 1
    
    print("Recaudación total: $" + f"{total_general:.2f}")