print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

#1-  Crear un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

informacion = {}  # Agregamos el diccionario vacio
bandera = 1       # Definimos la variable bandera como 1
while bandera == 1:  # Mientras que bandera sea igual a 1
    dato = str(input("¿Qué informacion vas a agregar? (nombre, edad, sexo, telefono, correo electronico, etc.)\n"))  
    # Pedimos la información que quiere agregar el usuario
    dato = dato.lower()  # Los datos introducidos serán convertidos a minúsculas gracias a lower.
    valor = str(input("Escribe el dato:\n"))  # Pedimos al usuario que ingrese el valor para el dato solicitado.
    informacion[dato] = valor  # Guardamos el dato y su valor en el diccionario.
    print(informacion)  # Mostramos el diccionario actualizado con los datos ingresados.
    print("¿Quieres seguir ejecutando el programa?\n Presiona 1 para continuar, de lo contrario presiona 2")  
    # Preguntamos si quiere seguir añadiendo información.
    bandera = int(input())  #solicitamos la bandera según la decisión del usuario (1 o 2).

print("FIN")  # Fin del programa cuando la bandera sea 2.
