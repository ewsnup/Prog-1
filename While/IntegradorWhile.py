# Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

contador = 0
negativos = 0
positivos = 0
sum_neg = 0
sum_pos = 0
max = None 
inicio = True

while inicio:
    num = int(input("Ingrese un número: "))
    contador += 1

    if max == None:
        max = num
    else:
        if num > max:
            max = num

    if num < 0:
        negativos += 1
        sum_neg += num

    if num > 0:
        positivos += 1
        sum_pos += num

    seguir = input("¿Desea seguir ingresando números? (S/N): ").upper()
    if seguir == "N":
        inicio = False

promedio = sum_pos / contador
porcentaje = sum_neg / contador * 100

print(f"La suma acumulada de los números negativos es de: {sum_neg}")
print(f"La suma acumulada de los números positivos es de: {sum_pos}")
print(f"La cantidad de números negativos ingresados es de: {negativos}")
print(f"El promedio de los números positivos es de: {promedio}")
print(f"El número positivo más grande: {max}")
print(f"El porcentaje de números negativos ingresados es de: {porcentaje}")