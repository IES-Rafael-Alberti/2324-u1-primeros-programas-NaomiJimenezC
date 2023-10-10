"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas 
que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

def calcular_peso_payaso(cantidad_payasos:int) -> int:
    peso_por_payaso = 112
    return peso_por_payaso * cantidad_payasos


def calcular_peso_munecas(cantidad_munecas:int) -> int:
    peso_por_muneca = 75
    return peso_por_muneca * cantidad_munecas

def calcular_peso_pedido(cantidad_payasos:int,cantidad_munecas) -> int:
    peso_total_payasos = calcular_peso_payaso(cantidad_payasos)
    peso_total_munecas = calcular_peso_munecas(cantidad_munecas)
    return peso_total_munecas + peso_total_payasos

if __name__ == "__main__":
    cantidad_munecas_pedidas = int(input("Cantidad de muñecas pedidas: "))
    cantidad_payasos_pedidos = int(input("Cantidad de payasos pedidos: "))

    peso_total = calcular_peso_pedido(cantidad_payasos_pedidos,cantidad_munecas_pedidas)

    print(f"La cantidad total del pedido es de {peso_total} gramos")