def crear_saludo(nombre: str):
    return "Hola," + nombre

nombre = input("Ingrese su nombre: ")

saludo_hecho = crear_saludo(nombre)

print(saludo_hecho)
