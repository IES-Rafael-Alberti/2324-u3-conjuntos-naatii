from src.ejercicio5 import *

def test_paresDeUnConjunto():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_result = {2, 4, 6, 8, 10}
    assert paresDeUnConjunto(numeros) == expected_result
def test_conjuntoMultiplosDeTres():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_result = {9, 3, 6}
    assert conjuntoDeMultiplosDeTres(numeros) == expected_result
def test_interseccionDeUnConjunto():
    numeros1 = {2, 4, 6, 8, 10}
    numeros2 = {9, 3, 6}
    expected_result = {6}
    assert interseccionDeUnConjunto(numeros1, numeros2) == expected_result