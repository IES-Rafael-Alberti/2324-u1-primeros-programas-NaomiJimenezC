"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

def imprimir_nombre(nombre_usuario:str, veces_a_repatir:int):
    for nombre in range(1, veces_a_repatir + 1):
        print (nombre_usuario)


if __name__ == '__main__':
    nombre = input("Ingrese un nombre: ")
    cantidad_repeticiones = int(input("Cantidad de repeticiones: "))

    imprimir_nombre(nombre, cantidad_repeticiones)
