import random

lineas = 3
coches_por_linea = 5
total_choferes = 15

def inicializar_matrices():
    matriz_recaudaciones = [
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0]
    ]
    

    legajos_choferes = [0] * total_choferes
    
    contador = 0
    while contador < total_choferes:
        legajo = random.randint(1000, 9999)
        existe = False

        i = 0
        while i < total_choferes:
            if legajos_choferes[i] == legajo:
                existe = True
                break
            i = i + 1
        
        if not existe:
            legajos_choferes[contador] = legajo
            contador = contador + 1
    
    return matriz_recaudaciones, legajos_choferes

def validar_legajo(legajo, legajos_choferes):
    i = 0
    while i < total_choferes:
        if legajos_choferes[i] == legajo:
            return True
        i = i + 1
    return False

def validar_linea_coche(linea, coche):
    if linea >= 1 and linea <= lineas and coche >= 1 and coche <= coches_por_linea:
        return True
    return False


def es_entero(valor):
    if valor == "":
        return False
    
    i = 0
    while i < len(valor):
        char = valor[i]
        if char < '0' or char > '9':
            return False
        i = i + 1
    return True

def es_decimal(valor):
    if valor == "":
        return False
    
    puntos = 0
    i = 0
    while i < len(valor):
        char = valor[i]
        if char == '.':
            puntos = puntos + 1
            if puntos > 1:
                return False
        elif char < '0' or char > '9':
            return False
        i = i + 1
    return True

def convertir_decimal(valor):
    pos_punto = -1
    i = 0
    while i < len(valor):
        if valor[i] == '.':
            pos_punto = i
            break
        i = i + 1
    
    if pos_punto == -1:
        resultado = 0
        i = 0
        while i < len(valor):
            char = valor[i]
            digito = int(char)
            resultado = resultado * 10 + digito
            i = i + 1
        return float(resultado)
    
    parte_entera = 0
    i = 0
    while i < pos_punto:
        char = valor[i]
        digito = int(char)
        parte_entera = parte_entera * 10 + digito
        i = i + 1
    
    parte_decimal = 0
    divisor = 1.0
    i = pos_punto + 1
    while i < len(valor):
        char = valor[i]
        digito = int(char)
        parte_decimal = parte_decimal * 10 + digito
        divisor = divisor * 10.0
        i = i + 1
    
    return parte_entera + (parte_decimal / divisor)

def cargar_recaudacion(matriz_recaudaciones, legajos_choferes):
    print("\n--- CARGAR RECAUDACIÓN ---")
    
    entrada_legajo = input("Ingrese número de legajo: ")
    if not es_entero(entrada_legajo):
        print("Error: El legajo debe ser un número entero")
        return matriz_recaudaciones
    
    legajo = int(convertir_decimal(entrada_legajo))
    if not validar_legajo(legajo, legajos_choferes):
        print("Error: Legajo no válido")
        return matriz_recaudaciones
    
    entrada_linea = input("Ingrese línea (1-3): ")
    if not es_entero(entrada_linea):
        print("Error: La línea debe ser un número")
        return matriz_recaudaciones
    
    linea = int(convertir_decimal(entrada_linea))
    
    entrada_coche = input("Ingrese coche (1-5): ")
    if not es_entero(entrada_coche):
        print("Error: El coche debe ser un número")
        return matriz_recaudaciones
    
    coche = int(convertir_decimal(entrada_coche))
    
    if not validar_linea_coche(linea, coche):
        print("Error: Línea o coche no válido")
        return matriz_recaudaciones
    
    entrada_recaudacion = input("Ingrese recaudación: $")
    if not es_decimal(entrada_recaudacion):
        print("Error: La recaudación debe ser un número válido")
        return matriz_recaudaciones
    
    recaudacion = convertir_decimal(entrada_recaudacion)
    
    if recaudacion < 0:
        print("Error: La recaudación no puede ser negativa")
        return matriz_recaudaciones
    
    matriz_recaudaciones[linea-1][coche-1] = matriz_recaudaciones[linea-1][coche-1] + recaudacion
    print("Recaudación cargada exitosamente")
    
    return matriz_recaudaciones

