#1.

i = 0

for i in range(1, 11):
    print(i)

# 2

i = 0
for i in range(10, 0, -1):
    print(i)

# 3

numero = int(input("Ingrese un numero: "))

for i in range(0, numero + 1):
   print(i)

# 4

num = int(input("Por favor ingrese un numero: "))


for i in range(1, 11):

    resultado = num * i
    print(f"{num} x {i} = {resultado}")

# 5

total = 0
promedio = 0


for i in range(10):
    num = int(input("Ingrese un número: "))
    print("El numero que usted ingresó es el: ", num)
    total = total + num
    if num == 0:
        break

if i != 0:
    promedio = total / i

print("promedio de los numeros ingresados es: ", promedio)
print("la suma de los numeros ingresados es: ", total)

# 6

for i in range(1, 3 + 1):
    print(3 * i)

# 7

for i in range(2, 51, 2):
    print(i)

# 8

num = int(input("Ingrese un numero: "))

for i in range(1, num + 1):
    for i in range(1, i + 1):
        print(i, end=" ")
    print()

# 9

num = int(input("Ingrese un número: "))

divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i) 
        divisores += 1

print("El número de divisores encontrados es:", divisores)

# 10

num = int(input("Ingrese un número: "))
primo = True

for i in range(1, num + 1):
    if i == 1:
        print(f"El numero {i} no es primo")
    else:
        numero = i
        for j in range(2, numero):
            if numero % j == 0:
                primo = False
                break
        else:
            primo = True

        if primo:
            print(f"El numero {i} es primo")
        else:
            print(f"El numero {i} no es primo")

# 11

num = int(input("Ingrese un número: "))
num_primo = 0

for i in range(1, num + 1):
    if i == 1:
        print(f"El numero {i} no es primo")
    else:
        primo = True  
        for j in range(2, i): 
            if i % j == 0:
                primo = False
                break
        
        if primo:
            print(f"El numero {i} es primo")
            num_primo += 1
        else:
            print(f"El numero {i} no es primo")

print("Números primos encontrados: ", num_primo)