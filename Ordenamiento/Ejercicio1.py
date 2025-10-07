"""
Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente.
La función debe implementar como algoritmo de ordenamiento el método de la burbuja. 
Además, como parámetro opcional debe recibir un booleano (que por default está en False),
que en caso de ser True ordena el vector en forma descendente.
"""
lista = [45, 64, 700, 23, 1, 4]

def ordenar_array(lista:list, descendente: bool = False) -> list:

    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if descendente:
                if(lista[i] < lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if(lista[i] > lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista

print("Original:", lista)
print("Ascendente:", ordenar_array(lista.copy()))
print("Descendente:", ordenar_array(lista.copy(), True))
print("Ascendente:", ordenar_array(lista.copy(), False))

