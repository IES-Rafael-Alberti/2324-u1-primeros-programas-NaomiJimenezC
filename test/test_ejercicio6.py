from src.ejercicios.ejercicio6 import *

def test_sacar_parte_iva():
    assert calcular_parte_iva(10.0) == 1

def test_sacar_precio_sin_iva():
    assert calcular_precio_sin_iva(10.0) == 9