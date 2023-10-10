##conversor de celsius a faregein##

def conversor_a_farenhei(grados_celsius:int,) -> float:
    return (grados_celsius * 9/5)+ 32

if __name__ == '__main__':
    grado_celsius = int(input("grado_celsius"))
    grados_farenheit = conversor_a_farenhei(grado_celsius)
    print(grados_farenheit)