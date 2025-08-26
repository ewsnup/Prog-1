# Una agencia de viajes nos pide informar si hacemos viajes a lugares
# según la estación del año. 

# En caso de hacerlo mostrar por print  el mensaje “Se viaja”,
# caso contrario mostrar “No se viaja”. 

# Si es invierno: solo se viaja a Bariloche.

# Si es verano: se viaja a Mar del plata y Cataratas.

# Si es otoño: se viaja a todos los lugares.

# Si es primavera: se viaja a todos los lugares menos Bariloche.

estacion = input("Ingrese la estación en la que desea viajar: ").lower()

match estacion:
    case "invierno":
        print("Se hacen viajes solamente a Bariloche.")
    case "verano":
        print("Se hacen viajes a Mar del plata y Cataratas.")
    case "otoño":
        print("Se hacen viajes a todos los destinos.")
    case "primavera":
        print("Se hacen viajes a todos los destinos MENOS Bariloche.")
    case _:
        print("Error. Intente de vuelta.")
