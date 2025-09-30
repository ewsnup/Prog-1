from Opcion1 import es_entero, convertir_decimal
lineas = 3
coches_por_linea = 5

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