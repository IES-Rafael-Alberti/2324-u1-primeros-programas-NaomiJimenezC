from src.ejercicios.ejercicio1 import crear_saludo

#tests ejercicio 1#
def test_imprimir_saludo():
    assert crear_saludo("Naomi") == "Hola,Naomi"