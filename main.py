#Version 2.0 31-Agosto-2023

# Declaracion de variables e inicializacion
import os
suma = 0
mayor = 0
menor = 32767   #Se coloca este rango porque es el tamaño máximo de un tipo dato entero
contador = 0
pares = 0
inpares = 0

while True:
    # Saber si el numero es valido (1)
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

    # Cuenta numeros inpares y pares ingresados en total mediante el módulo por valor ingresado
    if numero%2 == 1:
        pares += 1
    if numero%2 == 0:
        inpares+=1
    
    opc = input("¿Más datos?\n (S/N)\t")
    if opc=="N" or opc=="n":
        print("*"*30)
        break
    
    
promedio = suma/contador
print("Se ingresaron {} números".format(contador))
print("El promedio es ",promedio)
print("El número mayor ingresado es ",mayor)
print("El número menor ingresado es ",menor)
print("En total se ingresaron {} números inpares".format(inpares))
print("En total se ingresaron {} números pares".format(pares))
