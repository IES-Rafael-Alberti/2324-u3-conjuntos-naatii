from src.ejercicio4 import * 


def test_encontrarFrutas():
    frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    expected_result = {"manzana", "pera", "uva"}
    assert encontrarFrutas(frutas1, frutas2) == expected_result
def test_encontrarFrutasEnFrutas1PeroNoEnFrutas2():
    frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    expected_result = {'plátano', 'naranja'}
    assert encontrarFrutasEnFrutas1PeroNoEnFrutas2(frutas1, frutas2) == expected_result
def test_encontrarFrutasEnFrutas2PeroNoEnFrutas1():
    frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    expected_result = {'durazno', 'sandía'}
    assert encontrarFrutasEnFrutas2PeroNoEnFrutas1(frutas1, frutas2) == expected_result
