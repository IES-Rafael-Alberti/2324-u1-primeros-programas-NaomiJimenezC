"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.

Calcula el interés: capital * (1 + interes)
"""
def calcular_intereses(ahorros):
    porcentaje_interes = float("4%".replace("%",""))/100
    interes = ahorros * (1 + porcentaje_interes)
    return round(interes,2)

if __name__ == "__main__":
    capital_ahorrado = float(input("Ingrese sus ahorros: "))
    ahorro_primer_anyo = calcular_intereses(capital_ahorrado)
    ahorro_segundo_anyo = calcular_intereses(ahorro_primer_anyo)
    ahorro_tercer_anyo = calcular_intereses(ahorro_segundo_anyo)

    print(f"Ahorros primer año {ahorro_primer_anyo}, segundo año {ahorro_segundo_anyo} y tercer año {ahorro_tercer_anyo}")