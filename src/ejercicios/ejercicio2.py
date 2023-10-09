##Ejercicio 2##
def calcular_salario_por_hora(coste_por_hora:int,horas_trabajadas:int) -> int:
    return coste_por_hora * horas_trabajadas

horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
coste_por_hora = int(input("Ingrese el coste por horas trabajadas: "))

print (calcular_salario_por_hora(horas_trabajadas,coste_por_hora))