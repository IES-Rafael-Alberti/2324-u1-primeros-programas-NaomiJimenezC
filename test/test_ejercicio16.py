from src.ejercicios.ejercicio16 import calcular_precio_descuento,calcular_precio_sin_descuento

def test_calcular_precio_sin_descuento():
    assert calcular_precio_sin_descuento(50) == 174.5
def test_calcular_precio_descuento():
    assert calcular_precio_descuento(178.0) ==71.2

