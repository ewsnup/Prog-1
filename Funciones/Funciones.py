# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def solicitar_numero_entero() -> int:
    numero = int(input("Por favor, ingrese un número entero: "))
    return numero

numero = solicitar_numero_entero()
print(f"El número ingresado es: {numero}")

# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def solicitar_numero_flotante() -> float:
    numero = float(input("Por favor, ingrese un número flotante: "))
    return numero

numero = solicitar_numero_flotante()
print(f"El número ingresado es: {numero}")

# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def solicitar_una_cadena() -> str:
    texto = input("Por favor, ingrese un texto: ")
    return texto

texto = solicitar_una_cadena()
print(f"El texto ingresado es: {texto}")

# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def calcular_area_rectangular(base:float, altura:float) -> float:
    return base * altura

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area = calcular_area_rectangular(base, altura)
print(f"El área del rectangulo es de: {area}")

# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def calcular_area_circular(radio:int) -> int:
    return 2 * radio

radio = int(input("Ingrese el radio del círculo: "))

area = calcular_area_circular(radio)
print(f"El área del circulo es de: {area}")

# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_par_impar(numero:int) -> str:
    if numero % 2 == 0:
        mensaje = "El número es par"
    else:
        mensaje = "El número es impar"

    return mensaje

numero = int(input("Ingrese un número: "))
print(verificar_par_impar(numero))

# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def verificar_par_impar(numero:int) -> bool:
    if numero % 2 == 0:
        flag = True
    else:
        flag = False

    return flag

numero = int(input("Ingrese un número: "))
print(verificar_par_impar(numero))

# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_numero_maximo(num1:int, num2:int, num3:int) -> int:
    if (num1 > num2) and (num1 > num3):
        retorno = num1
    elif (num2 > num1) and (num2 > num3):
        retorno = num2
    else:
        retorno = num3
    
    return retorno

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))

max = encontrar_numero_maximo(num1, num2, num3)
print(f"El máximo de los tres números es: {max}")

# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base:int, exponente:int) -> int:
    return base ** exponente

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = calcular_potencia(base, exponente)
print(f"La potencia es de: {resultado}")

# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def determinar_numero_primo(numero:int) -> bool:
    retorno = True
    if numero == 1:
        retorno = False
    
    for i in range(2, numero):
        if numero % i == 0:
            retorno = False

    return retorno

num = int(input("Ingrese un número: "))
print(determinar_numero_primo(num))

# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad
#y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

def es_primo_simple(numero: int) -> bool:
    retorno = True
    if numero == 1:
        retorno = False
    
    for i in range(2, numero):
        if numero % i == 0:
            retorno = False
    
    return retorno

def encontrar_primos(limite: int) -> int:
    contador = 0
    
    print(f"Buscando primos hasta {limite}:")
    
    for num in range(1, limite + 1):
        if es_primo_simple(num):
            print(f"• {num} (primo)")
            contador += 1
        else:
            print(f"  {num}")
    
    return contador

limite = int(input("Ingrese el número límite: "))
total = encontrar_primos(limite)
print(f"\nTotal de números primos: {total}")


# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro.
#La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def mostrar_tabla(num: int, inicio: int = 1, fin: int = 10) -> None:
    print(f"\nTabla de multiplicar del {num} (del {inicio} al {fin}):")
    
    for i in range(inicio, fin + 1):
        resultado = num * i
        print(f"{num} × {i} = {resultado}")

seleccion = int(input("¿Desea que tenga inicio y fin? (1. si - 2. no): "))

if seleccion == 1:
    num = int(input("Ingrese el número: "))
    inicio = int(input("Ingrese desde qué número: "))
    fin = int(input("Ingrese hasta qué número: "))
    mostrar_tabla(num, inicio, fin)

else:
    num = int(input("Ingrese el número: "))
    mostrar_tabla(num) 