lineas = 3
coches_por_linea = 5


def mostrar_recaudacion_matriz(matriz_recaudaciones):
    print("\n--- RECAUDACIÓN POR COCHE Y LÍNEA ---")
    print("Línea/Coche   Coche 1   Coche 2   Coche 3   Coche 4   Coche 5")
    
    i = 0
    while i < lineas:
        linea_str = "Línea " + str(i+1) + "      "
        j = 0
        while j < coches_por_linea:
            valor = matriz_recaudaciones[i][j]
            linea_str = linea_str + "$" + f"{valor:7.2f}" + " "
            j = j + 1
        print(linea_str)
        i = i + 1