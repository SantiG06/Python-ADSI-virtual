# El comando IF
"""
num = int(input("Ingrese un numero: \n"))

if num == 100:
    print("Usted escribió el 100")
elif num > 100:
    print("Usted escribió un número mayor a 100")
else:
    print("Usted escribió un número menor a 100")
"""
# Condicionales multiples 

x = 5
if 0 < x:
    if x < 10:
        print("x es un número positivo de un solo digito.") # no recomendable

if 0 < x and x <10:
    print("x es un número positivo de un solo digito.") # recomendable

if 0 < x < 10:
    print("x es un número positivo de un solo digito.") # recomendable

