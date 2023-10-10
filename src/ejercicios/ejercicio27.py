"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y
muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros 
y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

def calcular_coste_total(unidades,precio_unitario)->str:
    precio_total = unidades * precio_unitario 
    return str(precio_total)


def parsear_precio_unitario(precio_unitario:str) -> str:
    precio_parseado = "{9.2f}".format(precio_unitario)
    return precio_parseado

def parsear_numero_unidades(numero_unidades:str) -> str:
    unidades_parseadas = "{:3d}".format(numero_unidades)
    return unidades_parseadas

def parsear_coste_total(coste_total:str) -> str:
    coste_total = "{:11.2f}".format(coste_total)
    return coste_total

if __name__ == '__main__':

    producto = input("Inserte el nombre del producto: ")
    cantidad_del_producto = int(input("Cantidad del producto: "))
    precio_unitario_producto = float(input("Precio unitario del producto: "))
    
    coste_total = calcular_coste_total(cantidad_del_producto, precio_unitario_producto)

    precio_unitario_parseado = parsear_precio_unitario(precio_unitario_producto)
    numero_unidades_parseado = parsear_numero_unidades(cantidad_del_producto)
    coste_total_parseado = parsear_coste_total(coste_total)

    print(f"Nombre del producto: {producto} precio unitario: {precio_unitario_parseado} , número de unidades: {numero_unidades_parseado} , coste total: {coste_total_parseado} euros")
    