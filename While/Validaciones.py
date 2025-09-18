# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave_correcta = "123"

clave = input("Por favor ingrese la clave: ") #123
while clave != clave_correcta:
    clave = input("Clave incorrecta. Por favor intente de vuelta: ")
print("La clave es correcta.")

# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

intentos = 1
clave_correcta = "123"

clave = input("Por favor ingrese la clave: ") #123
while clave != clave_correcta: 
    intentos += 1

    if intentos > 3:
        print("Se ha quedado sin intentos.")
        break

    clave = input("Clave incorrecta. Por favor intente de vuelta: ")

else:
    print("La clave es correcta.")

# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

nota = int(input("Ingrese una nota del 1 al 10: "))
while nota < 1 or nota > 10:
    nota = int(input("Error. Ingrese una nota del 1 al 10: "))
print("Nota ingresada.")

# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

color = input("Ingrese un Color (Rojo, Azul o Verde): ").lower()
while color != "rojo" and color != "azul" and color != "verde":
    color = input("Error. Ingrese un Color (Rojo, Azul o Verde): ")
print("Color ingresado.")