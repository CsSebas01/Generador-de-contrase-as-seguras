#Generador de contraseñas seguras
#importamos librerias
import string
import random

#Creamos variables
longitud = int(input("Ingrese el TAMAÑO de su contraseña: "))
#acci letters es para añadir tipos de letras y digitos.
caracteres = string.ascii_letters + string.digits + string.punctuation
#.join para concatenar letras de forma aleatoria con la libreria random y choice para seleccionar
contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es: " + contrasena)

#se puede mejorar poniendole condiciones 
