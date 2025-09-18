def listar_numeros(numeros: int) -> str | int:
    """
    Muestra todos los números en el orden ingresado
    """
    if len(numeros) == 0:
        print("No hay números para mostrar")
        return
    
    print("Números ingresados:")
    for i in range(len(numeros)):
        print(f"{i+1}. {numeros[i]}")

def listar_pares(numeros: int):
    """
    Muestra únicamente los números pares
    """
    from Especificas import es_par
    
    print("Números pares:")
    hay_pares = False
    
    for i in range(len(numeros)):
        if es_par(numeros[i]):
            print(f"{i+1}. {numeros[i]}")
            hay_pares = True
    
    if not hay_pares:
        print("No hay números pares")

def listar_posiciones_impares(numeros: int) -> str | int:
    """
    Muestra los números en posiciones impares (índices pares, ya que empieza en 0)
    """
    if len(numeros) == 0:
        print("No hay números para mostrar")
        return
    
    print("Números en posiciones impares:")
    for i in range(len(numeros)):
        if i % 2 == 0:  
            print(f"Posición {i+1}: {numeros[i]}")