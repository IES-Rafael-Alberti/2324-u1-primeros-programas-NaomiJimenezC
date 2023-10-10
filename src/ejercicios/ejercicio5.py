#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.#

def porcentaje_to_float(porcentaje:str)-> float:
    porcentaje_num = float(porcentaje.replace("%","").replace(',',"."))
    return porcentaje_num /100

def calculadora_iva(precio_sin_iva:float, tipo_iva:float) -> float:
    return (precio_sin_iva * tipo_iva) + precio_sin_iva

if __name__ == "__main__":
    precio_producto = int(input("Inserte el precio del producto sin iva: "))
    iva_a_aplicar = porcentaje_to_float(input("Inserte el porcentaje de iva a aplicar en el producto: "))
    precio_final = calculadora_iva(precio_producto,iva_a_aplicar)
    print(precio_final)