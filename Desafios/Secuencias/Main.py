from Ingresos import *
from Validaciones import *
from Secuencias import *
from Matriz import *

mostrar = True
while mostrar:
    print("""\nBienvenid@ al menú de opciones\n
1. Ingresar matriz manualmente
2. Generar matriz aleatoria
3. Salir del programa
""")
    
    opcion = int(input("Por favor escoja una opción del menú: "))

    match opcion:
        case 1:
            filas = get_int("Ingrese cantidad de filas (1-10): ", "Error: debe ser entre 1 y 10", 1, 10, 3)
            columnas = get_int("Ingrese cantidad de columnas (1-10): ", "Error: debe ser entre 1 y 10", 1, 10, 3)
            matriz = ingresar_matriz_manual(filas, columnas)
            mostrar_matriz(matriz)
            
            existe_secuencia, cantidad_secuencias, secuencia_mas_corta, secuencia_mas_larga = analizar_secuencias_pares(matriz)
            
            print("\n" + "-"*40)
            print("RESULTADOS DEL ANÁLISIS")
            print("-"*40)
            
            if existe_secuencia:
                print("Existen números consecutivos pares")
                print(f"Cantidad de secuencias encontradas: {cantidad_secuencias}")
                
                if len(secuencia_mas_corta) > 0:
                    print(f"\nSecuencia más corta ({len(secuencia_mas_corta)} números):")
                    secuencia_str = ""
                    for k in range(len(secuencia_mas_corta)):
                        secuencia_str = secuencia_str + str(secuencia_mas_corta[k]) + " "
                    print(secuencia_str)
                
                if len(secuencia_mas_larga) > 0:
                    print(f"\nSecuencia más larga ({len(secuencia_mas_larga)} números):")
                    secuencia_str = ""
                    for k in range(len(secuencia_mas_larga)):
                        secuencia_str = secuencia_str + str(secuencia_mas_larga[k]) + " "
                    print(secuencia_str)
            else:
                print("No existen números consecutivos pares")
                
        case 2:
            filas = get_int("Ingrese cantidad de filas (1-10): ", "Error: debe ser entre 1 y 10", 1, 10, 3)
            columnas = get_int("Ingrese cantidad de columnas (1-10): ", "Error: debe ser entre 1 y 10", 1, 10, 3)
            matriz = generar_matriz_aleatoria(filas, columnas)
            mostrar_matriz(matriz)
            
            existe_secuencia, cantidad_secuencias, secuencia_mas_corta, secuencia_mas_larga = analizar_secuencias_pares(matriz)
            
            print("\n" + "-"*40)
            print("RESULTADOS DEL ANÁLISIS")
            print("-"*40)
            
            if existe_secuencia:
                print("Existen números consecutivos pares")
                print(f"Cantidad de secuencias encontradas: {cantidad_secuencias}")
                
                if len(secuencia_mas_corta) > 0:
                    print(f"\nSecuencia más corta ({len(secuencia_mas_corta)} números):")
                    secuencia_str = ""
                    for k in range(len(secuencia_mas_corta)):
                        secuencia_str = secuencia_str + str(secuencia_mas_corta[k]) + " "
                    print(secuencia_str)
                
                if len(secuencia_mas_larga) > 0:
                    print(f"\nSecuencia más larga ({len(secuencia_mas_larga)} números):")
                    secuencia_str = ""
                    for k in range(len(secuencia_mas_larga)):
                        secuencia_str = secuencia_str + str(secuencia_mas_larga[k]) + " "
                    print(secuencia_str)
            else:
                print("No existen números consecutivos pares")
                
        case 3:
            print("¡Hasta luego!")
            print("\nSaliendo del programa...")
            mostrar = False
            
        case _:
            print("Opción no válida")