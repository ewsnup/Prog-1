from Resultados import mostrar_resultados


def main():
    print("""Sistema de Recomendación de Productos
\n¿Cómo desea ingresar los datos?
1. Usar listas predefinidas
2. Ingresar listas manualmente""")
    
    opcion = input("\nSeleccione una opción (1 o 2): ")
    
    if opcion == "1":

        usuario1 = "Ana"
        usuario2 = "Carlos"
        compras_ana = ["laptop", "mouse", "audífonos", "teclado"]
        compras_carlos = ["tablet", "mouse", "cargador", "audífonos"]
        
        mostrar_resultados(usuario1, usuario2, compras_ana, compras_carlos)
        
    elif opcion == "2":

        usuario1 = input("Nombre del primer usuario: ")
        usuario2 = input("Nombre del segundo usuario: ")
        
        print(f"\nIngrese los productos comprados por {usuario1} (separados por coma):")
        productos1 = input().split(",")
        compras1 = [producto.strip() for producto in productos1]
        
        print(f"\nIngrese los productos comprados por {usuario2} (separados por coma):")
        productos2 = input().split(",")
        compras2 = [producto.strip() for producto in productos2]
        
        mostrar_resultados(usuario1, usuario2, compras1, compras2)
        
    else:
        print("\nOpción no válida. Saliendo del programa.")

main()