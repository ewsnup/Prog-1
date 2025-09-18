def ingresar_numero(mensaje, min_val=-1000, max_val=1000) -> int:
    """
    Función para ingresar un número entero dentro de un rango específico
    """
    while True:
        entrada = input(mensaje)
        if entrada == '':
            print("Error: No puede estar vacío")
            continue
            
     
        es_numero = True
        if entrada[0] == '-':
           
            for caracter in entrada[1:]:
                if caracter < '0' or caracter > '9':
                    es_numero = False
                    break
        else:
          
            for caracter in entrada:
                if caracter < '0' or caracter > '9':
                    es_numero = False
                    break
        
        if not es_numero:
            print("Error: Debe ingresar un número entero")
            continue
        
       
        numero = 0
        if entrada[0] == '-':
            for i in range(1, len(entrada)):
                numero = numero * 10 + (ord(entrada[i]) - ord('0'))
            numero = -numero
        else:
            for i in range(len(entrada)):
                numero = numero * 10 + (ord(entrada[i]) - ord('0'))
        
  
        if numero < min_val or numero > max_val:
            print(f"Error: El número debe estar entre {min_val} y {max_val}")
            continue
        
        return numero

def ingresar_lista_numeros(cantidad=10) -> int:
    """
    Función para ingresar una lista de números
    """
    numeros = [0] * cantidad
    print(f"Ingrese {cantidad} números enteros entre -1000 y 1000:")
    
    for i in range(cantidad):
        numeros[i] = ingresar_numero(f"Número {i+1}: ")
    
    return numeros