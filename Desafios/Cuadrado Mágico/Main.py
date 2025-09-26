from Matriz_Manual import ingresar_matriz_manual
from Matriz_Aleatoria import generar_matriz_aleatoria
from Cuadrado_Magico import generar_cuadrado_magico_valido
from Verificar_Cuadrado import verificar_cuadrado_magico
from Mostrar_Matriz import mostrar_matriz

def main():
    print("-" * 50)
    print("         VERIFICADOR DE CUADRADO MÁGICO")
    print("-" * 50)
    
    n = obtener_orden_matriz()
    opcion = obtener_opcion_menu()
    matriz = crear_matriz_segun_opcion(n, opcion)
    mostrar_resultados(matriz, n)

def obtener_orden_matriz() -> int:
    """Obtiene y valida el orden de la matriz"""
    n = 0
    while n <= 0:
        print("\nIngrese el orden de la matriz (n): ")
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
            n = 0
        else:
            n = int(entrada)
            if n <= 0:
                print("Error: El orden debe ser mayor a 0")
                n = 0
    return n

def obtener_opcion_menu() -> int:
    """Obtiene y valida la opción del menú"""
    print("\nSeleccione el método de ingreso:")
    print("1. Ingreso manual")
    print("2. Generar matriz aleatoria")
    print("3. Generar cuadrado mágico válido")
    
    opcion = 0
    while opcion < 1 or opcion > 3:
        print("Opción (1-3): ")
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
        else:
            opcion = int(entrada)
            if opcion < 1 or opcion > 3:
                print("Error: Seleccione una opción válida (1-3)")
                opcion = 0
    return opcion

def crear_matriz_segun_opcion(n, opcion) -> int:
    """Crea la matriz según la opción seleccionada"""
    matriz = None
    
    match opcion:
        case 1:
            matriz = ingresar_matriz_manual(n)
        case 2:
            matriz = generar_matriz_aleatoria(n)
        case 3:
            matriz = generar_cuadrado_magico_valido(n)
    
    if type(matriz) != list:
        print("Error: No se pudo crear la matriz")
        return None
    
    return matriz

def mostrar_resultados(matriz, n):
    """Muestra la matriz y verifica si es cuadrado mágico"""
    if matriz is None or type(matriz) != list:
        return
    
    mostrar_matriz(matriz)
    
    constante_magica = n * (n*n + 1) // 2
    print(f"\nConstante mágica esperada: {constante_magica}")
    
    if verificar_cuadrado_magico(matriz, constante_magica):
        print("¡La matriz ES un cuadrado mágico!")
    else:
        print("La matriz NO es un cuadrado mágico")

main()