#Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, pregunte al usuario por
# un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto. Si el producto no
# está en el diccionario debe mostrar un mensaje informando de ello.



producto = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
articulo = input("Introduce el articulo que desees: ")
unidad = int(input("Introduce cuantas unidades desea: "))

if articulo in producto:
    print(float((producto[articulo] * unidad)))