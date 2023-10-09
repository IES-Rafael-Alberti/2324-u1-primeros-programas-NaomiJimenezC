"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

def desglosar_fecha(fecha_str):
    partes_fecha = fecha_str.split('/')
    
    if len(partes_fecha) == 3:
        dia, mes, año = partes_fecha
        
        dia = int(dia)
        mes = int(mes)
        año = int(año)
        
        return dia, mes, año


if __name__ == '__main__':

    fecha = input("Ingrese una fecha con este formato: dd/mm/yyyy: ")
    
    fecha_parseada = desglosar_fecha(fecha)
    