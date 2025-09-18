# Contadores - Acumuladores - Máximos y mínimos

# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

contador = 10
while contador >= 1:
    print(contador)
    contador -= 1

# Mostrar la suma de los números desde el 1 hasta el 10.

contador = 1
suma = 0

while contador <= 10:
    suma += contador
    print(contador)
    contador +=1

print(f"La suma total es de: {suma}")

# Mostrar la suma de los números pares desde el 1 hasta el 10.

contador = 1
suma = 0

while contador <= 10:
    if contador % 2 == 0:
        suma += contador

    contador += 1

print(f"La suma total es de: {suma}")

# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

ingreso = 1
suma = 0

while ingreso <= 5:
    num = int(input("Ingrese un número: "))
    suma += num
    ingreso += 1
    promedio = suma // 5

print(f"La suma total es de: {suma}")
print(f"El promedio es de: {promedio}")

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

ingreso = True
contador = 0
suma = 0

while ingreso:
    num = int(input("Ingrese un número: "))
    suma += num
    contador += 1

    seguir = input("¿Desea seguir ingresando números? (S/N): ").upper()
    if seguir == "N":
        ingreso = False

promedio = suma // contador

print(f"\nCantidad de números ingresados: {contador}")
print(f"La suma total es de: {suma}")
print(f"El promedio es de: {promedio}")

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

ingreso = True
positivos = 0
negativos = 1
hay_negativos = False

while ingreso:
    num = int(input("Ingrese un número: "))
    
    if num > 0:
        positivos += num
    elif num < 0:
        negativos *= num
        hay_negativos = True

    seguir = input("¿Desea seguir ingresando números? (S/N): ").upper()
    if seguir == "N":
        ingreso = False

print(f"Suma de números positivos: {positivos}")

if hay_negativos:
    print(f"Producto de números negativos: {negativos}")
else:
    print("No hay números negativos.")

# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contador = 1
max = None
min = None

while contador <= 10:
    num = int(input("Ingrese un número: "))

    if max == None:
        max = num
        min = num
    else:
        if num > max:
            max = num
    
    if num < min:
            min = num

    contador += 1

print(f"El máximo es: {max}")
print(f"El mínimo es: {min}")

# Anexo:
# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

ingreso = True
contador = 0
suma = 0

print("Debe ingresar mínimo 5 números.\n")

while ingreso:
    num = int(input("Ingrese un número: "))
    suma += num
    contador += 1

    if contador >= 5:
        seguir = input("¿Desea seguir ingresando números? (S/N): ").upper()
        if seguir == "N":
            ingreso = False

promedio = suma // contador

print(f"\nCantidad de números ingresados: {contador}")
print(f"La suma de los números ingresados es de: {suma}")
print(f"El promedio es de: {promedio}")

# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

ingreso = True
contador = 0
suma = 0

print("Debe ingresar como mínimo 5 números y como máximo 10 números.\n")

while ingreso and contador < 10:
    num = int(input("Ingrese un número: "))
    suma += num
    contador += 1

    if contador >= 5 and contador < 10:
        seguir = input("¿Desea seguir ingresando números? (S/N): ").upper()
        if seguir == "N":
            ingreso = False

promedio = suma // contador

print(f"\nCantidad de números ingresados: {contador}")
print(f"La suma de los números ingresados es de: {suma}")
print(f"El promedio es de: {promedio}")