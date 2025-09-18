#1.

def sumar_naturales(num:int)->int:
    '''
    la funcion se llama a sí misma con el numero ingresado
    restandole 1 hasta llegar a 0 
    '''
    if num == 0:
        return 0
    else:
        return num + sumar_naturales (num - 1)
    

num1 = int(input("Ingrese un numero: "))
print(f"La suma de {num1} es de: {sumar_naturales(num1)}")

#2.

def calcular_potencia(base: int, exponente:int)->int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"La potencia de {base} elevado a {exponente} es de: {calcular_potencia(base, exponente)}")

#3.

def sumar_digitos(num:int)->int:
    '''
    Si el numero es de un digito se devuelve ese numero
    De lo contrario se saca el el ultimo digito del numero
    Luego elimina el ultimo digito diviendo el numero entero por 10
    '''
    if num < 10:
        return num
    return (num % 10) + sumar_digitos(num // 10)

numero = int(input("Ingrese un numero: "))
print(f"La suma de los digitos de {numero} es de: {sumar_digitos(numero)}")

#4.

def calcular_numero_fibonacci(numero:int)->int:
    if numero == 0 or numero == 1:
        return numero
    else:
        return calcular_numero_fibonacci (numero - 1) + calcular_numero_fibonacci (numero - 2)

numero = int(input("Ingrese un numero: "))

print(calcular_numero_fibonacci(numero))