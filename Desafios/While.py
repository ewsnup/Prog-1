# 📌 Desafío: Encuesta Tecnológica en UTN Technologies
# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.
# Las tecnologías en evaluación son:
#  🔹 Inteligencia Artificial (IA)
#  🔹 Realidad Virtual/Aumentada (RV/RA)
#  🔹 Internet de las Cosas (IOT)
# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
# 🔹 Recolección de Datos
# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)
# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
# 🔹 Análisis de Datos
# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.
# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.

#edad
may_edad = None

#generos
hombre = 0
mujer = 0
otro = 0

#tecnologias
IA = 0
RV = 0
IOT = 0

#cuentas
uno = 0
dos = 0
tres = 0

ingreso = 0

print("¡Bienvenido/a a la encuesta Tecnológica en UTN Technologies!")
print("Por favor, ingrese sus datos: ")

while ingreso < 10:
    #Datos
    nombre = input("\nIngrese su nombre: ")

    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("Su edad no es válida, intente de nuevo: "))

    genero = input("Ingrese su género (Hombre/Mujer/Otro): ").upper()
    if genero == "HOMBRE":
        hombre += 1
    elif genero == "OTRO":
        otro += 1
    while genero != "HOMBRE" and genero != "MUJER" and genero != "OTRO":
        genero = input("Error. Ingrese su género (Hombre/Mujer/Otro): ").upper()

    tecno = input("Ingrese la técnologia elegida (IA/RV/IOT): ").upper()
    if tecno == "IA":
        IA += 1
    elif tecno == "RV":
        RV += 1
    else:
        IOT += 1
    while tecno != "IA" and tecno != "RV" and tecno != "IOT":
        tecno = input("Error. Ingrese la técnologia elegida (IA/RV/IOT): ")

    ingreso += 1


    # 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
    if genero == "HOMBRE":
        if edad >= 25 and edad <= 50:
            if tecno == "IOT" or tecno == "IA":
                uno += 1

    # 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
    # Su género no sea Femenino y su edad está entre los 33 y 40 años.
    if genero != "MUJER":
        if edad >= 33 and edad <= 40:
            if tecno != "IA":
                dos += 1

    # 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.
    if genero == "HOMBRE":
        if may_edad == None or edad > may_edad:
            may_edad = edad
            nombre_mayor_edad = nombre
            tecno_mayor_edad = tecno

porcentaje = (dos / ingreso) * 100

print(f"\nNúmero de empleados masculinos que votaron por IOT o IA, entre 25 y 50 años: {uno}")
print(f"Porcentaje de empleados no mujeres que NO votaron por IA, entre 33 y 40 años: {porcentaje}")
print(f"El empleado de mayor edad es {nombre}, con {edad} años y votó por {tecno}")