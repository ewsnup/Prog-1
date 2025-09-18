# Integrador Validaciones
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.


print("¡Bienvenido/a al Censo Nacional!")
print("\nPor favor, proceda con la carga de datos...\n")

apellido = input("Por favor ingrese su apellido: ").upper()

edad = int(input("Por favor ingrese su edad: "))
while edad < 18 or edad > 90:
    print("Su edad es invalida. Debe tener entre 18 y 90 años.")
    edad = int(input("Por favor ingrese su edad: "))
    
estados_validos = ["SOLTERO", "CASADO", "DIVORCIADO", "VIUDO", "SOLTERA", "CASADA", "DIVORCIADA", "VIUDA"]
estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ").upper()
while estado_civil not in estados_validos:
    print("Estado civil inválido. Por favor ingrese: Soltero/a, Casado/a, Divorciado/a o Viudo/a")
    estado_civil = input("Ingrese su estado civil: ").upper()

while True:
    legajo = input("Escriba su número de legajo: ")
    
    if len(legajo) < 4:
        print("Faltan números. Debe tener 4 cifras")
    elif len(legajo) > 4:
        print("Sobran números. Debe tener solo 4 cifras")
    elif legajo[0] == "0":
        print("No puede empezar con cero")
    else:
        break

print("\nCargando datos...")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado Civil: {estado_civil}")
print(f"Legajo: {legajo}")
