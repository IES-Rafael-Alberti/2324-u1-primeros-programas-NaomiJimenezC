"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.
"""



if __name__ == "__main__":

    nombre_usuario = input("Inserte su nombre de usuario: ")
    cantidad_letras = nombre_usuario.count()
    nombre_mayuscula =  nombre_usuario.upper()

    print(f"{nombre_mayuscula} tiene {cantidad_letras} letras")