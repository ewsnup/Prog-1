import random
from FuncionesPPT import *

def jugar_piedra_papel_tijera() -> str:
    """
    Gestiona toda la lógica del juego Piedra, Papel o Tijera.
    
    Retorno:
        str: "Jugador" o "Máquina" indicando el ganador de la partida
    """
    print("=" * 50)
    print("BIENVENIDO A PIEDRA, PAPEL O TIJERA")
    print("=" * 50)
    print("Reglas: Mejor de 3 rondas. 2 victorias seguidas terminan la partida.")
    print("=" * 50)
    
    # Inicializar contadores
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0
    victorias_seguidas_jugador = 0
    victorias_seguidas_maquina = 0
    
    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
        ronda_actual += 1
        print(f"\n🔹 RONDA {ronda_actual}")
        print("-" * 30)
        
        # Obtener elecciones
        eleccion_jugador = obtener_eleccion_jugador()
        eleccion_maquina = random.randint(1, 3)
        
        print(f"Jugador elige: {mostrar_elemento(eleccion_jugador)}")
        print(f"Máquina elige: {mostrar_elemento(eleccion_maquina)}")
        
        
        if verificar_ganador(eleccion_jugador, eleccion_maquina) == "Jugador":
            aciertos_jugador += 1
            victorias_seguidas_jugador += 1
            victorias_seguidas_maquina = 0
            print("🏆 ¡Gana el Jugador!")
        elif verificar_ganador(eleccion_jugador, eleccion_maquina) == "Máquina":
            aciertos_maquina += 1
            victorias_seguidas_maquina += 1
            victorias_seguidas_jugador = 0
            print("Gana la Máquina!")
        else:
            victorias_seguidas_jugador = 0
            victorias_seguidas_maquina = 0
            print("Empate!")
        
        # Mostrar marcador
        print(f"\nMarcador: Jugador {aciertos_jugador} - {aciertos_maquina} Máquina")
        
        # Verificar victorias seguidas
        if victorias_seguidas_jugador >= 2:
            print("¡Jugador gana por 2 victorias seguidas!")
            break
        elif victorias_seguidas_maquina >= 2:
            print("Máquina gana por 2 victorias seguidas!")
            break
    
    # Determinar ganador final
    ganador_final = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    
    print("\n" + "=" * 50)
    print("FIN DE LA PARTIDA")
    print("=" * 50)
    print(f"Marcador Final: Jugador {aciertos_jugador} - {aciertos_maquina} Máquina")
    
    if ganador_final == "Jugador":
        print("¡FELICIDADES! Has ganado la partida!")
    else:
        print("La Máquina ha ganado la partida. ¡Inténtalo de nuevo!")
    
    print("=" * 50)
    
    return ganador_final

jugar_piedra_papel_tijera()