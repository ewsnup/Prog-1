"""
Desafío: Sistema de Recomendación de Productos
Una tienda online quiere mejorar su sistema de recomendaciones analizando el comportamiento de sus clientes.
Para ello, dispone del historial de compras de dos usuarios distintos, almacenado en listas de productos.
📌 Objetivo: Escribir un programa en Python que permita analizar estos historiales de compra y responder las siguientes preguntas:
 1️⃣ Productos en común: ¿Qué productos han comprado ambos usuarios?
 2️⃣ Productos exclusivos: ¿Qué productos ha comprado cada usuario que el otro no ha adquirido?
 3️⃣ Catálogo total: ¿Cuál sería el conjunto total de productos comprados entre los dos usuarios?
 4️⃣ Recomendaciones: ¿Cómo podrías utilizar esta información para sugerir productos a cada usuario?
🎯 Requisitos:
 ✔️ El programa debe recibir como entrada dos listas de productos (pueden ser ingresadas manualmente o predefinidas).
 ✔️ Debe procesar y mostrar los resultados de forma clara.
 ✔️ Se valorará el uso de funciones para estructurar el código de manera organizada.
🔹 Extras opcionales:
Permitir que los usuarios ingresen sus listas manualmente.
Ampliar el programa para comparar más de dos usuarios.
"""

def encontrar_comunes(lista1, lista2):
    comunes = []
    for producto in lista1:
        encontrado = False
        i = 0
        while i < len(lista2) and not encontrado:
            if producto == lista2[i]:
                comunes = comunes + [producto]
                encontrado = True
            i = i + 1
    return comunes

def encontrar_unicos(lista1, lista2):
    unicos = []
    for producto in lista1:
        encontrado = False
        i = 0
        while i < len(lista2) and not encontrado:
            if producto == lista2[i]:
                encontrado = True
            i = i + 1
        if not encontrado:
            unicos = unicos + [producto]
    return unicos

def combinar_listas(lista1, lista2):
    combinada = lista1[:]
    for producto in lista2:
        encontrado = False
        i = 0
        while i < len(combinada) and not encontrado:
            if producto == combinada[i]:
                encontrado = True
            i = i + 1
        if not encontrado:
            combinada = combinada + [producto]
    return combinada

# Función para mostrar resultados
def mostrar_resultados(usuario1, usuario2, lista1, lista2):
    print("\n" + "-"*50)
    print(f"Análisis de compras: {usuario1} vs {usuario2}")
    print("-"*50)
    
    # Productos en común
    comunes = encontrar_comunes(lista1, lista2)
    print(f"\n1️. Productos en común: {comunes}")
    
    # Productos exclusivos
    unicos1 = encontrar_unicos(lista1, lista2)
    unicos2 = encontrar_unicos(lista2, lista1)
    print(f"\n2️. Productos exclusivos de {usuario1}: {unicos1}")
    print(f"   Productos exclusivos de {usuario2}: {unicos2}")
    
    # Catálogo total
    catalogo = combinar_listas(lista1, lista2)
    print(f"\n3️. Catálogo total de productos: {catalogo}")
    
    # Recomendaciones
    print(f"\n4️. Recomendaciones:")
    print(f"   Para {usuario1}: podría interesarle {unicos2}")
    print(f"   Para {usuario2}: podría interesarle {unicos1}")

# Función principal
def main():
    print("""Sistema de Recomendación de Productos
\n¿Cómo desea ingresar los datos?
1. Usar listas predefinidas
2. Ingresar listas manualmente""")
    
    opcion = input("\nSeleccione una opción (1 o 2): ")
    
    if opcion == "1":

        usuario1 = "Ana"
        usuario2 = "Carlos"
        compras_ana = ["laptop", "mouse", "audífonos", "teclado"]
        compras_carlos = ["tablet", "mouse", "cargador", "audífonos"]
        
        mostrar_resultados(usuario1, usuario2, compras_ana, compras_carlos)
        
    elif opcion == "2":

        usuario1 = input("Nombre del primer usuario: ")
        usuario2 = input("Nombre del segundo usuario: ")
        
        print(f"\nIngrese los productos comprados por {usuario1} (separados por coma):")
        productos1 = input().split(",")
        compras1 = [producto.strip() for producto in productos1]
        
        print(f"\nIngrese los productos comprados por {usuario2} (separados por coma):")
        productos2 = input().split(",")
        compras2 = [producto.strip() for producto in productos2]
        
        mostrar_resultados(usuario1, usuario2, compras1, compras2)
        
    else:
        print("\nOpción no válida. Saliendo del programa.")

main()