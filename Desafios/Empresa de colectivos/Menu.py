from Opcion1 import *
from Opcion2 import mostrar_recaudacion_matriz
from Opcion3 import calcular_recaudacion_por_linea
from Opcion4 import calcular_recaudacion_por_coche
from Opcion5 import calcular_recaudacion_total


matriz_recaudaciones, legajos_choferes = inicializar_matrices()
    
print("Sistema de gestión de recaudaciones inicializado.")
print("Legajos generados:", legajos_choferes)

mostrar = True
while mostrar:
    print("""\nBienvenid@ al menú de opciones\n
1. Cargar planilla de recaudación
2. Mostrar la recaudación de cada coche y linea
3. Calcular y mostrar la recaudación por linea
4. Calcuar y mostrar la recaudación por noche
5. Calcular y mostrar la recaudación total
6. Salir del programa
""")
    
    opcion = int(input("\nPor favor escoja una opción del menú: "))

    match opcion:
            case 1:
                matriz_recaudaciones = cargar_recaudacion(matriz_recaudaciones, legajos_choferes)
            case 2:
                mostrar_recaudacion_matriz(matriz_recaudaciones)
            case 3:
                calcular_recaudacion_por_linea(matriz_recaudaciones)
            case 4:
                calcular_recaudacion_por_coche(matriz_recaudaciones)
            case 5:
                calcular_recaudacion_total(matriz_recaudaciones)
            case 6:
                print("¡Hasta luego!")
                print("\nSaliendo del programa...")
                mostrar = False
            case _:
                print("Opción no válida")