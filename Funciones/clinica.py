def ingresar_datos_paciente() -> str:
    """
    Solicita al usuario que ingrese los datos médicos del paciente por consola.
    
    Retorna:
            - nombre (str): Nombre del paciente
            - peso (float): Peso en kilogramos
            - altura (float): Altura en metros
            - temperatura (float): Temperatura corporal en °C
            - presion_sistolica (float): Presión arterial sistólica
            - presion_diastolica (float): Presión arterial diastólica
    """

    print("=== INGRESO DE DATOS DEL PACIENTE ===")
    nombre = input("Nombre del paciente: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    temperatura = float(input("Temperatura (°C): "))
    presion_sistolica = float(input("Presión sistólica: "))
    presion_diastolica = float(input("Presión diastólica: "))
    
    return nombre, peso, altura, temperatura, presion_sistolica, presion_diastolica

def cargar_consulta(nombre_paciente: str, peso: float, altura: float, temperatura: float, presion_sistolica: float, presion_diastolica: float) -> str:
    """
    Genera un diagnóstico médico completo integrando los análisis de todas las funciones especializadas.
    
    Parámetros:
        nombre_paciente (str): Nombre del paciente
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
        temperatura (float): Temperatura corporal en °C
        presion_sistolica (float): Presión arterial sistólica
        presion_diastolica (float): Presión arterial diastólica
    
    Retorna:
        str: Diagnóstico médico completo formateado con todos los análisis
    """

    # Llamar a las otras funciones
    analisis_temperatura = temperatura_paciente(temperatura)
    analisis_peso = peso_paciente(peso, altura)
    analisis_presion = presion_paciente(presion_sistolica, presion_diastolica)
    
    # Calcular IMC para mostrarlo
    imc = peso / (altura ** 2)
    
    diagnostico = f"""
    Diagnóstico del paciente {nombre_paciente}:
    Peso: {peso} kg, Altura: {altura} m, IMC: {imc} - {analisis_peso}
    Temperatura: {temperatura}°C - {analisis_temperatura}
    Presión arterial: {presion_sistolica}/{presion_diastolica} mmHg - {analisis_presion}
    """
    
    return diagnostico

def temperatura_paciente(temperatura: float) -> str:
    """
    Analiza la temperatura corporal y devuelve una evaluación clínica.
    
    Parámetro:
        temperatura (float): Temperatura corporal en °C
    
    Retorna:
        str: Evaluación de la temperatura según rangos clínicos establecidos:
            - > 41°C: "Muy alta."
            - 39-41°C: "Alta."
            - 38-39°C: "Fiebre moderada."
            - 37.3-38°C: "Febrícula."
            - ≤ 37.3°C: "Temperatura normal."
    """

    if temperatura > 41:
        fiebre = "Muy alta."
    elif temperatura > 39:
        fiebre = "Alta."
    elif temperatura >= 38:
        fiebre = "Fiebre moderada."
    elif temperatura > 37.3:
        fiebre = "Febrícula."
    else:
        fiebre = "Temperatura normal."
    
    return fiebre

def peso_paciente(peso: float, altura: float) -> str:
    """
    Analiza el peso del paciente calculando el IMC y devuelve una recomendación nutricional.
    
    Parámetro:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    
    Retorna:
        str: Recomendación nutricional basada en el IMC:
            - IMC < 18.5: "Es necesario aumentar ingesta calórica."
            - IMC 18.5-25: "Peso equilibrado."
            - IMC > 25: "Es necesario disminuir ingesta calórica."
    """

    # Calcular Índice de Masa Corporal (IMC)
    imc = peso / (altura ** 2)
    
    # Evaluar el IMC según rangos establecidos por la OMS
    if imc < 18.5:
        analisis_imc = "Es necesario aumentar ingesta calórica."
    elif imc < 25:
        analisis_imc = "Peso equilibrado."
    else:
        analisis_imc = "Es necesario disminuir ingesta calórica."

    return analisis_imc

def presion_paciente(presion_sistolica: float, presion_diastolica: float) -> str:

    """
    Evalúa la presión arterial y determina su estado clínico.
    
    Parámetros:
        presion_sistolica (float): Presión arterial sistólica (máxima)
        presion_diastolica (float): Presión arterial diastólica (mínima)
    
    Retorna:
        str: Estado de la presión arterial:
            - "Baja": Si sistólica < 90 o diastólica < 60
            - "Alta": Si sistólica > 140 o diastólica > 90
            - "Normal": Valores dentro del rango normal
    """

    if presion_sistolica < 90 or presion_diastolica < 60:
        analisis_presion = "Baja"
    elif presion_sistolica > 140 or presion_diastolica > 90:
        analisis_presion = "Alta"
    else:
        analisis_presion = "Normal"
    
    return analisis_presion


# ===== PROGRAMA PRINCIPAL =====
# Ingresar datos del paciente mediante la función de entrada
datos_paciente = ingresar_datos_paciente()

# Generar el diagnóstico médico completo integrando todos los análisis
resultado = cargar_consulta(*datos_paciente)
    
# Mostrar el resultado formateado con separadores visuales
print("\n" + "="*60)
print(resultado)
print("="*60)
