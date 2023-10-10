#escribe un programa que devuelva el resto y cociente de una división#

def sacar_elementos_division(dividendo:int,divisor:int):
    cociente = dividendo / divisor
    resto = dividendo // divisor
    return (cociente,resto)

if __name__ == "__main__":
    
    dividendo = int(input("Ingrese un número entero acá: "))
    divisor = int(input("Ingrese un número entero acá: "))

    cociente_resto = sacar_elementos_division(dividendo,divisor)

    print(f"La división entre {dividendo} y {divisor} da de conciente {cociente_resto[0]} y de resto {cociente_resto[1]}")