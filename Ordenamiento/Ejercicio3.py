"""
Crear una función que reciba como parámetro un vector de números enteros.
La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente.

"""

lista = [-1, 3, 56, -76, -89, 34, 17, -22]

def mostrar_numeros_ordenados(lista: list):

    positivos = []
    negativos = []

    for num in lista:
        if num < 0:
            negativos = negativos + [num]
        else:
            positivos = positivos + [num]

    for i in range(len(positivos)-1):
        for j in range(i + 1, len(positivos)):
            if(positivos[i] > positivos[j]):
                aux = positivos[i]
                positivos[i] = positivos[j]
                positivos[j] = aux

    for i in range(len(negativos)-1):
            for j in range(i + 1, len(negativos)):
                if(negativos[i] < negativos[j]):
                    aux = negativos[i]
                    negativos[i] = negativos[j]
                    negativos[j] = aux

    resultado = []
    for num in negativos:
        resultado = resultado + [num]
    
    for num in positivos:
        resultado = resultado + [num]
    
    return resultado

print("Resultado:", mostrar_numeros_ordenados(lista))