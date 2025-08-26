# Calcular una nota aleatoria entre el 1 y el 10 inclusive, 
# para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

import random

nota = random.randint(1, 10)

if nota <= 3:
    print(f"Desaprobado, su nota es {nota}")
elif nota == 4 or nota == 5:
    print(f"Aprobado, su nota es {nota}")
else:
    print(f"Promoción directa, su nota es {nota}")
    