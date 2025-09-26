from comunes import *

def mostrar_resultados(usuario1, usuario2, lista1, lista2):
    print("\n" + "-"*50)
    print(f"Análisis de compras: {usuario1} vs {usuario2}")
    print("-"*50)
    

    comunes = encontrar_comunes(lista1, lista2)
    print(f"\n1️. Productos en común: {comunes}")
    

    unicos1 = encontrar_unicos(lista1, lista2)
    unicos2 = encontrar_unicos(lista2, lista1)
    print(f"\n2️. Productos exclusivos de {usuario1}: {unicos1}")
    print(f"   Productos exclusivos de {usuario2}: {unicos2}")
    

    catalogo = combinar_listas(lista1, lista2)
    print(f"\n3️. Catálogo total de productos: {catalogo}")
    

    print(f"\n4️. Recomendaciones:")
    print(f"   Para {usuario1}: podría interesarle {unicos2}")
    print(f"   Para {usuario2}: podría interesarle {unicos1}")

