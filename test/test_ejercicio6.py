from src.ejercicio6 import *

def test_crearSubconjunto():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r','s', 't', 'v', 'w', 'x', 'y', 'z'}
    assert crearSubconjunto(vocales, consonantes) == {'a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r','s', 't', 'v', 'w', 'x', 'y', 'z'}