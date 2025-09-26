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

