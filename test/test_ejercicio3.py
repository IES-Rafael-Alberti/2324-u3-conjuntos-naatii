from src.ejercicio3 import *
import pytest

@pytest.mark.parametrize(
    "conjunto, expected",
    [
        (
            {1, 2, 3},
            [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
        ),
        (
            {4, 3, 2, 6},
            [set(), {2}, {3}, {2, 3}, {4}, {2, 4}, {3, 4}, {2, 3, 4}, {6}, {2, 6}, {3, 6}, {2, 3, 6}, {4, 6}, {2, 4, 6}, {3, 4, 6}, {2, 3, 4, 6}]
        ),
    ]
)

def test_todosLosSubconjuntos(conjunto, expected):
    assert todosLosSubconjuntos(conjunto) == expected