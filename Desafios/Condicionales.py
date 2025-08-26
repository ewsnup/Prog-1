# Facturación del Servicio de Agua Potable

# Tarifa base:
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.

# Bonificaciones y Recargos según tipo de cliente:
# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
# En todos los casos, se aplica el IVA del 21% sobre el total.

# Requerimientos del programa:
# Solicitar al usuario:
# Cantidad de metros consumidos
# Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
# Calcular:
# Subtotal de consumo.
# Bonificaciones, si corresponde
# Recargos, si corresponde
# Subtotal, con recargos y bonificaciones.
# IVA aplicado (21%), si corresponde.
# Total final a pagar.
# Mostrar en pantalla el desglose de los cálculos.

tarifa = 7000
costo_m3 = 200
porcentaje_iva = 0.21

print("\nBienvenido a la Facturación del Servicio de Agua Potable.")
consumo = int(input("Por favor ingrese la cantidad de metros cubicos consumidos: "))
tipo_cliente = input("Por favor ingrese el tipo de cliente (Residencial, Comercial o Industrial): ").lower()

costo_consumo = costo_m3 * consumo
bonificacion = 0
recargo = 0 

match tipo_cliente:
    case "residencial":
        if consumo < 30:
            print("\nSe le aplica una bonificación del 10%")
            bonificacion = costo_consumo * 0.10
            costo_consumo -= bonificacion
        elif consumo > 80:
            print("\nSe le aplica un recargo del 15%")
            recargo = costo_consumo * 0.15
            costo_consumo += recargo

    case "comercial":
        if consumo < 50:
            print("\nSe le aplica un recargo del 5%")
            recargo = costo_consumo * 0.05
            costo_consumo -= recargo
        elif consumo < 300:
            print("\nSe le aplica una bonificación del 8%")
            bonificacion = costo_consumo * 0.08
            costo_consumo -= bonificacion
        else:
            print("\nSe le aplica una bonificación del 12%")
            bonificacion = costo_consumo * 0.12
            costo_consumo -= bonificacion
        
    case "industrial":
        if consumo < 200:
            print("\nSe le aplica un recargo del 10%")
            recargo = costo_consumo * 0.10
            costo_consumo -= recargo
        elif consumo < 1000:
            print("\nSe le aplica una bonificación del 20%")
            bonificacion = costo_consumo * 0.20
            costo_consumo -= bonificacion
        else:
            print("\nSe le aplica una bonificación del 30%")
            bonificacion = costo_consumo * 0.30
            costo_consumo -= bonificacion

cost_mod = costo_consumo - bonificacion + recargo

desc_ad = 0
if tipo_cliente == "residencial" and (costo_consumo + tarifa) < 35000:
    print("\nSe aplica un descuento adicional del 5%")
    desc_ad = (cost_mod + tarifa) * 0.05

subtotal = cost_mod + tarifa - desc_ad
iva = subtotal * porcentaje_iva
total = subtotal + iva


print("\nDesgloce:")
print(f"Consumo: {consumo} m³")
print(f"Costo por consumo: ${costo_consumo}")
print(f"Bonificacion: -${bonificacion}")
print(f"Recargo: +${recargo}")
print(f"Descuento adicional: -${desc_ad}")
print(f"Cargo fijo: +${tarifa}")
print(f"Subtotal antes de IVA: ${subtotal}")
print(f"IVA (21%): +${iva}")
print(f"Cargo final: {total}")
