from src.ejercicio2 import * 
import pytest

@pytest.mark.parametrize(
    "alumnosPrimaria, alumnosSecundaria, salida",
    [
        (
            {"marta", "maria", "rafa"},
            {"marta", "maria", "carlos"},
            {"marta", "maria", "rafa", "carlos"}
        )
    ]
)
def test_todosLosAlumnos(alumnosPrimaria, alumnosSecundaria, salida):
    assert todosLosAlumnos(alumnosPrimaria, alumnosSecundaria) == salida

@pytest.mark.parametrize(
    "alumnosPrimaria, alumnosSecundaria, salida",
    [
        (
            {"marta", "maria", "rafa"},
            {"marta", "maria", "carlos"},
            {"marta", "maria"}
        )
    ]
)
def test_alumnosRepetidos(alumnosPrimaria, alumnosSecundaria, salida):
    assert alumnosRepetidos(alumnosPrimaria, alumnosSecundaria) == salida

@pytest.mark.parametrize(
    "alumnosPrimaria, alumnosSecundaria, salida",
    [
        (
            {"marta", "maria", "rafa"},
            {"marta", "maria", "carlos"},
            {"rafa"}
        )
    ]
)
def test_alumnosNoRepetidos(alumnosPrimaria, alumnosSecundaria, salida):
    assert alumnosNoRepetidos(alumnosPrimaria, alumnosSecundaria) == salida

@pytest.mark.parametrize(
    "alumnoPrimaria, alumnoSecundaria, salida",
    [
        (
            {"marta", "maria", "rafa"},
            {"marta", "maria", "carlos"},
            False
        )
    ]
)
def test_alumnosPrimariaIncluidosEnSecundaria(alumnoPrimaria, alumnoSecundaria, salida):
    assert alumnosPrimariaIncluidosEnSecundaria(alumnoPrimaria, alumnoSecundaria) == salida