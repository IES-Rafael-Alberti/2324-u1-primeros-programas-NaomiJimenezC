#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.#
contador = 0
lista_sumando = []
while contador != 3:
    lista_sumando.append(int(input("Ingrese un número: ")))
    contador +=1

print(sum(lista_sumando))