def mostrar_matriz(matriz):
    """Mostrar la matriz de forma organizada"""
    if type(matriz) != list:
        print("Error: Matriz no válida")
        return
    
    n = len(matriz)
    print("\nMatriz ingresada:")
    print("-" * (n * 5))
    
    for i in range(n):
        if type(matriz[i]) != list:
            print("Error: Fila no válida")
            return
        
        for j in range(n):
            print(f"{matriz[i][j]:4d}", end=" ")
        print()
    
    print("-" * (n * 5))