"""
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el 
nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""

def convert_to_Mayus(nombre:str) -> str:
    return nombre.upper()
def convert_to_minus(nombre:str) -> str:
    return nombre.lower()
def convert_to_capitalize(nombre:str) -> str:
    return nombre.title()

if __name__ == "__main__":
    nombre = input("Ingrese su nombre aquí: ")
    print(f"Nombre en mayúsculas {convert_to_Mayus(nombre)}\n Nombre en minúscula: {convert_to_minus(nombre)} \n  Nombre capitalizado{convert_to_capitalize(nombre)}")