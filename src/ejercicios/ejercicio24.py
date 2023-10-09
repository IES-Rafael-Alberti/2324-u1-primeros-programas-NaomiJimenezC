"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla
el número de euros y el número de céntimos del precio introducido.
"""

def desglosar_precio(precio:str):
    precio_float = float(precio)
    euros = int(precio_float)
    centimos = int((precio_float - euros) * 100)  
    return euros, centimos

if __name__ == '__main__':
    precio_producto = input("Inserte el precio del producto: ")

    euros = desglosar_precio(precio_producto)
    euros_separados = euros[0]
    centimos = euros[1]

    print(f"son {euros_separados} euros y {centimos} centimos")