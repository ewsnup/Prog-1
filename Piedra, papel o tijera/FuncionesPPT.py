def verificar_ganador(jugador:int, maquina:int) -> str:
    
    if jugador == maquina:
        retorno = "Empate"

    # Piedra VS Tijera
    if jugador == 1 and maquina == 3:
        retorno = "Jugador"
    if maquina == 1 and jugador == 3:
        retorno = "Maquina"
    
    # Papel VS Piedra
    if jugador == 2 and maquina == 1:
        retorno = "Jugador"
    if maquina == 2 and jugador == 1:
        retorno = "Maquina"
    
    # Tijera VS Papel
    if jugador == 3 and maquina == 2:
        retorno = "Jugador"
    if maquina == 3 and jugador == 2:
        retorno = "Maquina"

    return retorno

def verificar_estado_partida(aciertos_jugador:int, aciertos_maquina:int, ronda_actual:int) -> bool:
    retorno = True
        # Si alguien tiene 2 victorias seguidas, la partida termina
    if aciertos_jugador >= 2 and aciertos_maquina == 0:
        retorno = False
    if aciertos_maquina >= 2 and aciertos_jugador == 0:
        retorno = False
    
    # Si ya se jugaron 3 rondas y hay un ganador claro
    if ronda_actual >= 3:
        if aciertos_jugador > aciertos_maquina or aciertos_maquina > aciertos_jugador:
            retorno = False
    
    # Si hay empate después de 3 rondas, se continúa
    return retorno

def verificar_ganador_partida(aciertos_jugador:int, aciertos_maquina:int) -> str:

    if aciertos_jugador > aciertos_maquina:
        retorno = "Jugador"
    else:
        retorno = "Máquina"
    
    return retorno

def mostrar_elemento(eleccion:int) -> str:
    
    if eleccion == 1:
        retorno = "Piedra"
    elif eleccion == 2:
        retorno = "Papel"
    elif eleccion == 3:
        retorno = "Tijera"
    else:
        retorno = "Desconocido"

    return retorno

def obtener_eleccion_jugador():

    while True:
        print("\nElige tu elemento:")
        print("1 - Piedra")
        print("2 - Papel")
        print("3 - Tijera")
            
        eleccion = int(input("Tu elección (1-3): "))
            
        if eleccion in [1, 2, 3]:
            return eleccion
        else:
            print("Error: Por favor ingresa solo 1, 2 o 3")

