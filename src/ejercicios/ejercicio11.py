"""
    Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre
en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
"""

def calcular_num_enteros_hasta(numero_introducido_usuario: int):
    return int((numero_introducido_usuario*(numero_introducido_usuario+1))/2)

if __name__ == '__main__':
    
    numero_positivo = int(input("Ingrese un número entero positivo: "))
    if numero_positivo:
        for numero in range(1,calcular_num_enteros_hasta(numero_positivo)+1):
            print(numero)
    else:
        print("Pon un número entero positivo")