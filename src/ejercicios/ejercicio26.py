"""
Escribir un programa que pregunte por consola por los productos
de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
def splitear_lista_compra(lista_compra:str) -> list:
    lista_compra_parseada = lista_compra.split(',')
    return lista_compra_parseada

def imprimir_lista_compra(lista_compra_parseadas:list):
    for i in lista_compra_parseadas:
        print(i)


if __name__ == '__main__':
    lista_compra = input("Ingrese una lista de la compra: ")
    lista_compra_parseada = splitear_lista_compra(lista_compra)

    imprimir_lista_compra(lista_compra_parseada)
