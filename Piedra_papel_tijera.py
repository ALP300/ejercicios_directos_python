'''
PIEDRA, PAPEL O TIJERA
'''
import random

def piedra_papel_tijera():
    opciones=["piedra","papel","tijera"]
    print("Bienvenido a Piedra, papel y tijera")
    
    while True:
        usuario= input("Elige piedra, papel, tijera (o escribe salir para terminar): ")
        if usuario=="salir":
            print("Gracias por jugar")
            break
    
        if usuario not in opciones:
            print("OPCIÓN INVÁLIDA, INTENTA NUEVAMENTE")
            continue
        
        computadora= random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        
        if usuario==computadora:
            print("Es un empate")
        
        elif(usuario=="piedra" and computadora=="tijera") or \
            (usuario=="papel" and computadora=="piedra") or \
            (usuario=="tijera" and computadora=="papel"):
                print("Ganaste")
        
        else:
            print("Perdiste, más suerte a la próxima")

piedra_papel_tijera()
            
        