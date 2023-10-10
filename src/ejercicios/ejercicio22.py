"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal
, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

def vocal_to_mayus(frase:str,vocal:str):
    vocales = ["a","e","i","o","u"]
    frase_final = ""
    for letra in frase:
        if letra == vocal and letra in vocales:
            frase_final += letra.upper()
        else:
            frase_final += letra 
    return frase_final


if __name__ == "__main__":

    frase = input("Frase: ")
    vocal = input("Vocal: ")

    print(vocal_to_mayus(frase,vocal))