from src.ejercicios.ejercicio5 import calculadora_iva,porcentaje_to_float


def test_sacada_porcentaje_con_coma():
    assert porcentaje_to_float("9,5%") == 0.095

def test_sacada_porcentaje_con_punto():
    assert porcentaje_to_float("9.5%") == 0.095