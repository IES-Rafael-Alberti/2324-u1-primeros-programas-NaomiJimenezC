"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
"""

from ejercicio5 import porcentaje_to_float

PRECIO_BARRA_PAN ="3.49€"

def calcular_precio_sin_descuento(cantidad_pan:int) -> float:
    precio_pan = float(PRECIO_BARRA_PAN.replace("€",""))
    return cantidad_pan * precio_pan

def calcular_precio_descuento(precio_sin_descuento:float) -> float:
    descuento = porcentaje_to_float("60%")
    precio_descuento = precio_sin_descuento - (precio_sin_descuento * descuento)
    return precio_descuento

if __name__ == "__main__":
    cantidades_de_panes_que_no_son_del_dia = int(input("Ingrese la cantidad de panes que no son del día:  "))

    precio_sin_descuento = calcular_precio_sin_descuento(cantidades_de_panes_que_no_son_del_dia)
    precio_panes_descuento = calcular_precio_descuento(precio_sin_descuento)

    print(f"El precio del pan del día es de {PRECIO_BARRA_PAN}")
    print(f"El precio con descuento de {cantidades_de_panes_que_no_son_del_dia} panes que no son del día es de {precio_panes_descuento} ")