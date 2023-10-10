"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
import re


def comprobar_formato_numerico(formato_num:str):
    regex_tlf = r'^\+\d{2}-\d{9}-\d{2}$'
    matching_tlf = re.match(regex_tlf, formato_num)
    
    if matching_tlf != None:
        return True

def parser_tlf(tlf:str):
    if comprobar_formato_numerico(tlf):
        return tlf[4:13]
    
    
if __name__ == '__main__':

    num_tlf = input("Ingrese un número de tlf con el siguiente formato: +34-913724710-56 : ")
    num_parseado = parser_tlf(num_tlf)

    print(num_parseado)