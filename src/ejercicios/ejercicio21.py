"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""

def invetir_frase(frase:str):
    return frase[::-1]


if __name__ == '__main__':
    frase_a_introducir = input("Introduzca una frase: ")

    frase_invertida = invetir_frase(frase_a_introducir)

    print(frase_invertida)