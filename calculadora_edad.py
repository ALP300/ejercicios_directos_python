'''
Pregunta: Calculadora de Edad
Crea una calculadora que reciba la fecha de nacimiento 
de un usuario y calcule su edad exacta hasta la fecha actual.
Además, haz que te dé una recomendación basada en la edad 
(por ejemplo, "Podrías comenzar a aprender a programar"
si tienes menos de 20 años).

'''

from datetime import datetime

def calculadora_edad():
    fecha_nacimiento= input("INGRESA TU FECHA DE NACIMIENTO (DD/MM/AAAA): ")
    try:
        fecha_nacimiento= datetime.strptime(fecha_nacimiento,"%d/%m/%Y")
        hoy= datetime.now()       
        edad= hoy.year - fecha_nacimiento.year-((hoy.month,hoy.day)<(fecha_nacimiento.month, fecha_nacimiento.day))
        print(f"Tienes {edad} años.")
        
    except ValueError:
        print("Por favor, ingresa una fecha correcta")
    
    if edad<20:
        print("Podrías comenzar a programar, nunca es tarde")
    
    elif 20 <= edad <35:
        print("Es un gran momento para empezar")
    
    elif 35 <= edad <60:
        print("Es un momento momento para enseñar lo que sabes")
    
    else:
        print("Nunca es tarde para aprender")

calculadora_edad()
    
    









