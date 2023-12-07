#Version 1.0 29-Agosto-2023

# Declaracion de variables e inicializacion
import os
suma = 0
mayor = 0
menor = 32767   #Se coloca este rango porque es el tamaño máximo de un tipo dato entero
contador = 0

while True:
    # Saber si el numero es valido
    while True:
        numero = int(input("Ingresa un número: "))
        if (numero<0 or numero>32767):
            print("El número ingresado es inválido")
        else:
            os.system('clear')
            break
    
    contador +=1
    suma+=numero
    
    # Encuentra el menor o mayor numero ingresado
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    
    opc = input("¿Más datos?\n (S/N)\t")
    if opc=="N" or opc=="n":
        print("*"*30)
        break
    
    
promedio = suma/contador
print("Se ingresaron {} números".format(contador))
print("El promedio es ",promedio)
print("El número mayor ingresado es ",mayor)
print("El número menor ingresado es ",menor)
