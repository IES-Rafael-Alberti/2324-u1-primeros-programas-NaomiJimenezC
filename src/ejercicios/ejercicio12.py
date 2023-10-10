#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.#

def calcular_imc(peso:int,estatura:float) -> float:
    return round((peso/estatura)**2,2)

if __name__ == "__main__":
    peso = int(input("Ingrese su peso en kilos: "))
    estatura = float(input("Ingrese su estatura en metros: "))

    imc = calcular_imc(peso,estatura)

    print(f"Su IMC es de {imc}")