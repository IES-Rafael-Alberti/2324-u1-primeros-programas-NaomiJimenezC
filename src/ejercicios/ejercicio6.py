#Escribe un programa que pida el importe final de un artículo y calcule e imprima#
#por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).#

from src.ejercicios.ejercicio5 import porcentaje_to_float 

def calcular_parte_iva(precio_con_iva:float) -> float:
    porcentaje_iva = "10%"
    return porcentaje_to_float(porcentaje_iva) * precio_con_iva


def calcular_precio_sin_iva(precio_con_iva:float) -> float:
    precio_sin_iva = precio_con_iva - calcular_parte_iva(precio_con_iva) 
    return precio_sin_iva


if __name__ == "__main__":
    precio_con_iva = float("Ingrese el precio del producto: ")
    print(f"El precio sin iva es de {calcular_precio_sin_iva} y la parte que corresponde al iva es de {calcular_parte_iva}")