'''
Descripción: Escribe un programa donde la computadora
elija un número aleatorio entre 1 y 100, y el usuario
tenga que adivinarlo.

Si el número ingresado es mayor al número secreto, 
dile al usuario "Muy alto".
Si es menor, dile "Muy bajo".
Continúa hasta que el usuario adivine correctamente.
'''
import random

def adivina_el_numero():
    numero_secreto= random.randint(1,100)
    intentos=0
    print("¡ADIVINA UN NÚMERO QUE ESTÁ ENTRE 1-100!")
    
    while True:
        intento= int(input("Tu intento: "))
        intentos+=1
        
        if intento<numero_secreto:
            print("Muy baja")
        
        elif intento>numero_secreto:
            print("Muy alto")
        else:
            print(f"¡FELICIDADES ADIVINASTE EN {intentos} intentos")
            break
            

adivina_el_numero()