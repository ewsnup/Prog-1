from Input import ingresar_lista_numeros
from Especificas import contar_positivos_negativos, sumar_pares, mayor_impar
from Array_Generales import listar_numeros, listar_pares, listar_posiciones_impares

def mostrar_menu():

    print("\n" + "-"*50)
    print("MENÚ DE OPCIONES")
    print("-"*50)
    print("1️. Ingresar datos (10 números enteros)")
    print("2️. Cantidad de positivos y negativos")
    print("3️. Suma de los números pares")
    print("4️. Mayor número impar")
    print("5️. Listar los números ingresados")
    print("6️. Listar los números pares")
    print("7️. Listar números en posiciones impares")
    print("8️. Salir del programa")
    print("-"*50)

def main():

    numeros = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")
        
        # Validación simple y directa
        if opcion == '1':
            numeros = ingresar_lista_numeros(10)
            print("Datos ingresados correctamente")
            
        elif opcion == '2':
            if len(numeros) == 0:
                print("Primero debe ingresar los datos (opción 1)")
            else:
                positivos, negativos = contar_positivos_negativos(numeros)
                print(f"Positivos: {positivos}")
                print(f"Negativos: {negativos}")
                
        elif opcion == '3':
            if len(numeros) == 0:
                print("Primero debe ingresar los datos (opción 1)")
            else:
                suma = sumar_pares(numeros)
                print(f"Suma de números pares: {suma}")
                
        elif opcion == '4':
            if len(numeros) == 0:
                print("Primero debe ingresar los datos (opción 1)")
            else:
                mayor = mayor_impar(numeros)
                if mayor is None:
                    print("No hay números impares")
                else:
                    print(f"Mayor número impar: {mayor}")
                    
        elif opcion == '5':
            if len(numeros) == 0:
                print("Primero debe ingresar los datos (opción 1)")
            else:
                listar_numeros(numeros)
                
        elif opcion == '6':
            if len(numeros) == 0:
                print("Primero debe ingresar los datos (opción 1)")
            else:
                listar_pares(numeros)
                
        elif opcion == '7':
            if len(numeros) == 0:
                print("Primero debe ingresar los datos (opción 1)")
            else:
                listar_posiciones_impares(numeros)
                
        elif opcion == '8':
            print("¡Gracias por usar el programa!")
            break
            
        else:
            print("Opción no válida. Debe ingresar un número entre 1 y 8")


main()