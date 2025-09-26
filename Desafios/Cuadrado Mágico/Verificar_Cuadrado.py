def verificar_cuadrado_magico(matriz, constante_magica):
    """Verificar si es cuadrado mágico"""
    if type(matriz) != list:
        return False
    
    n = len(matriz)
    es_magico = True
    
    # Verificar filas
    for i in range(n):
        if type(matriz[i]) != list:
            return False
        
        suma_fila = 0
        for j in range(n):
            suma_fila = suma_fila + matriz[i][j]
        
        if suma_fila != constante_magica:
            es_magico = False
            break
    
    # Verificar columnas
    if es_magico:
        for j in range(n):
            suma_columna = 0
            for i in range(n):
                suma_columna = suma_columna + matriz[i][j]
            
            if suma_columna != constante_magica:
                es_magico = False
                break
    
    # Verificar diagonal principal
    if es_magico:
        suma_diagonal = 0
        for i in range(n):
            suma_diagonal = suma_diagonal + matriz[i][i]
        
        if suma_diagonal != constante_magica:
            es_magico = False
    
    # Verificar diagonal secundaria
    if es_magico:
        suma_diagonal = 0
        for i in range(n):
            suma_diagonal = suma_diagonal + matriz[i][n-1-i]
        
        if suma_diagonal != constante_magica:
            es_magico = False
    
    return es_magico