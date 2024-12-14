'''
Dinámica 4: Generador de contraseñas 
seguras
Descripción: El programa genera una 
contraseña aleatoria de una longitud 
especificada por el usuario.
'''
import random
import string

def generador_contraseñas():
    longitud= int(input("¿De cuántas caracteres quieres tu contraseña?: "))
    caracteres= string.ascii_letters+string.digits+string.punctuation
    contraseña= ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Tu contraseña es: {contraseña}")
    
generador_contraseñas()