def ingresar_matriz_manual(n) -> list:
    print(f"\nIngrese los valores para una matriz {n}x{n}:")
    print(f"Los valores deben ser enteros únicos entre 1 y {n*n}")
    

    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila = fila + [0]
        matriz = matriz + [fila]
    

    numeros_usados = []
    for i in range(n*n + 1):
        numeros_usados = numeros_usados + [0]
    
    for i in range(n):
        for j in range(n):
            valor_valido = False
            while not valor_valido:
                print(f"Fila {i+1}, Columna {j+1}: ")
                entrada = input()
                

                es_numero = True
                if entrada == "":
                    es_numero = False
                else:
                    for caracter in entrada:
                        if caracter < '0' or caracter > '9':
                            es_numero = False
                            break
                
                if not es_numero:
                    print("Error: Ingrese un número entero válido")
                    continue
                
                valor = int(entrada)

                if valor < 1 or valor > n*n:
                    print(f"Error: El valor debe estar entre 1 y {n*n}")
                    continue

                if numeros_usados[valor] == 1:
                    print("Error: Este número ya fue ingresado")
                else:
                    matriz[i][j] = valor
                    numeros_usados[valor] = 1
                    valor_valido = True
    
    return matriz