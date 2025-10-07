"""
Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, y devuelva un único vector también ordenado.
La función debe tener un parámetro opcional descendente para que el vector resultante esté en orden descendente.
"""

lista1 = [32, 56, 76, 20, 15]
lista2 = [130, 3, 96, 44, 6]

def intercalar_vectores(lista1: list, lista2: list, descendente: bool = False) -> list:
    for i in range(len(lista1) - 1):
        for j in range(i + 1, len(lista1)):
            if(lista2[i] > lista2[j]):
                    aux = lista2[i]
                    lista2[i] = lista2[j]
                    lista2[j] = aux
    
    for i in range(len(lista2) - 1):
        for j in range(i + 1, len(lista2)):
            if(lista1[i] > lista1[j]):
                    aux = lista1[i]
                    lista1[i] = lista1[j]
                    lista1[j] = aux
    
def intercalar_vectores(lista1: list, lista2: list, descendente: bool = False) -> list:
    tamaño_total = len(lista1) + len(lista2)
    resultado = [0] * tamaño_total
    
    k = 0  
    i = 0  
    j = 0  
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado[k] = lista1[i]
            i += 1
        else:
            resultado[k] = lista2[j]
            j += 1
        k += 1
    
    while i < len(lista1):
        resultado[k] = lista1[i]
        i += 1
        k += 1
    
    while j < len(lista2):
        resultado[k] = lista2[j]
        j += 1
        k += 1
    
    if descendente:
        izquierda = 0
        derecha = len(resultado) - 1
        while izquierda < derecha:
            resultado[izquierda], resultado[derecha] = resultado[derecha], resultado[izquierda]
            izquierda += 1
            derecha -= 1
    
    return resultado

lista1 = [32, 56, 76, 20, 15]
lista2 = [130, 3, 96, 44, 6]

print("Vector 1 original:", lista1)
print("Vector 2 original:", lista2)

resultado_asc = intercalar_vectores(lista1, lista2)
print("Intercalado ascendente:", resultado_asc)

resultado_desc = intercalar_vectores(lista1, lista2, descendente=True)
print("Intercalado descendente:", resultado_desc)

    
