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

def calcular_recaudacion_por_coche(matriz_recaudaciones):
    print("\n--- RECAUDACIÓN POR COCHE ---")
    
    entrada_coche = input("Ingrese número de coche (1-5): ")
    if not es_entero(entrada_coche):
        print("Error: Debe ingresar un número válido")
        return
    
    coche = int(convertir_decimal(entrada_coche))
    
    if coche < 1 or coche > coches_por_linea:
        print("Error: Coche no válido")
        return
    
    total_coche = 0.0
    i = 0
    while i < lineas:
        total_coche = total_coche + matriz_recaudaciones[i][coche-1]
        i = i + 1
    
    print("Recaudación total del Coche " + str(coche) + ": $" + f"{total_coche:.2f}")

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

def mostrar_menu():
    print("\n" + "="*40)
    print("SISTEMA DE GESTIÓN DE RECAUDACIONES")
    print("="*40)
    print("1. Cargar planilla de recaudación")
    print("2. Mostrar recaudación por coche y línea")
    print("3. Calcular recaudación por línea")
    print("4. Calcular recaudación por coche")
    print("5. Calcular recaudación total")
    print("6. Salir")
    print("="*40)

def main():
    # Inicializar matrices
    matriz_recaudaciones, legajos_choferes = inicializar_matrices()
    
    print("Sistema de gestión de recaudaciones inicializado")
    print("Legajos generados:", legajos_choferes)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                matriz_recaudaciones = cargar_recaudacion(matriz_recaudaciones, legajos_choferes)
            case "2":
                mostrar_recaudacion_matriz(matriz_recaudaciones)
            case "3":
                calcular_recaudacion_por_linea(matriz_recaudaciones)
            case "4":
                calcular_recaudacion_por_coche(matriz_recaudaciones)
            case "5":
                calcular_recaudacion_total(matriz_recaudaciones)
            case "6":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida")

main()