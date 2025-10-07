from Validaciones import es_par

def encontrar_secuencias_en_fila(fila: list) -> list:
    """
    Encuentra todas las secuencias de números pares consecutivos en una fila
    """
    secuencias_fila = []
    secuencia_actual = []
    en_secuencia = False
    columnas = len(fila)
    
    for j in range(columnas):
        if es_par(fila[j]):
            if not en_secuencia:
                secuencia_actual = [fila[j]]
                en_secuencia = True
            else:
                nueva_secuencia = [0] * (len(secuencia_actual) + 1)
                for k in range(len(secuencia_actual)):
                    nueva_secuencia[k] = secuencia_actual[k]
                nueva_secuencia[len(secuencia_actual)] = fila[j]
                secuencia_actual = nueva_secuencia
        else:
            if en_secuencia and len(secuencia_actual) >= 2:
                secuencias_fila = secuencias_fila + [secuencia_actual]
            en_secuencia = False
            secuencia_actual = []
    
    if en_secuencia and len(secuencia_actual) >= 2:
        secuencias_fila = secuencias_fila + [secuencia_actual]
    
    return secuencias_fila

def encontrar_todas_secuencias(matriz: list) -> list:
    """
    Encuentra todas las secuencias de números pares consecutivos en toda la matriz
    """
    todas_secuencias = []
    filas = len(matriz)
    
    for i in range(filas):
        secuencias_fila = encontrar_secuencias_en_fila(matriz[i])
        if len(secuencias_fila) > 0:
            for secuencia in secuencias_fila:
                todas_secuencias = todas_secuencias + [secuencia]
    
    return todas_secuencias

def existe_algunas_secuencias(secuencias: list) -> bool:
    """
    Verifica si existen secuencias de números pares consecutivos
    """
    return len(secuencias) > 0

def encontrar_secuencia_mas_corta(secuencias: list) -> list:
    """
    Encuentra la secuencia más corta de números pares consecutivos
    """
    if len(secuencias) == 0:
        return []
    
    secuencia_mas_corta = secuencias[0]
    for i in range(1, len(secuencias)):
        if len(secuencias[i]) < len(secuencia_mas_corta):
            secuencia_mas_corta = secuencias[i]
    
    return secuencia_mas_corta

def encontrar_secuencia_mas_larga(secuencias: list) -> list:
    """
    Encuentra la secuencia más larga de números pares consecutivos
    """
    if len(secuencias) == 0:
        return []
    
    secuencia_mas_larga = secuencias[0]
    for i in range(1, len(secuencias)):
        if len(secuencias[i]) > len(secuencia_mas_larga):
            secuencia_mas_larga = secuencias[i]
    
    return secuencia_mas_larga

def analizar_secuencias_pares(matriz: list):
    """
    Función principal que coordina el análisis de secuencias pares
    """
    if len(matriz) == 0:
        return False, 0, [], []
    
    todas_secuencias = encontrar_todas_secuencias(matriz)
    
    existe_secuencia = existe_algunas_secuencias(todas_secuencias)
    cantidad_secuencias = len(todas_secuencias)
    secuencia_mas_corta = encontrar_secuencia_mas_corta(todas_secuencias)
    secuencia_mas_larga = encontrar_secuencia_mas_larga(todas_secuencias)
    
    return existe_secuencia, cantidad_secuencias, secuencia_mas_corta, secuencia_mas_larga