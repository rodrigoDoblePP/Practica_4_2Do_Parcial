# 2-Hacer un diccionario de traducción español-inglés, se van a introducir las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas.

print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

diccionario = {}  # Inicializo un diccionario vacío donde se van a guardar las palabras y sus traducciones

palabras = input("Escribe las palabras como en el siguiente formato -hola:hello,perro:dog,casa:house-: \n")  
# Pedimos al usuario que ingrese varias palabras con sus traducciones separadas por comas y ops puntos.

for i in palabras.split(","):  # Recorro cada par de palabras separadas por comas.
    
    clave, valor = i.split(":")  
    # Cada palabra lo separo usando ":" para tener la palabra en españolque es (clave) y su traducción que es(valor).
    
    diccionario[clave] = valor  
    # Guardamos la palabra en español como clave y su traducción como valor en el diccionario.

frase = input("Escribe una frase en español para traducirla \n")  
# Le pedimos al usuario que escriba una frase en español para poderla traducir.

for j in frase.split(" "):  # Recorre cada palabra de la frase separada por espacios.
    
    if j in diccionario:   # Si la palabra está en el diccionario
        
        print(diccionario[j], end=" ")  
        # Imprime la palabra traducida agregando un espacio.

    else:    # Si la palabra no está en el diccionario, imprimo la palabra original.
        
        print(j, end=" ")   #Imprime la palabra en español agregando un espacio.
        
