#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se
# añada un nuevo dato debe imprimirse el contenido del diccionario.


diccionario = {}
continuar = True
while continuar:
    clave = input("¿Que datos quieres guardar?: ")
    valor = input(clave + " --> ")
    diccionario[clave] = valor
    print(diccionario)
    continuar = input("¿Quieres seguir introduciendo datos si/no?: ") == "si"