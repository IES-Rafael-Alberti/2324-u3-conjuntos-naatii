from src.ejercicio1 import *
import pytest    
# The function receives a list of tuples with client information and returns a set with all the unique addresses.
@pytest.mark.parametrize(
        "clientes, expected",  
        [
            (
                [
                    ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
                    ("Jorge Russo", 7, 699, "Mirasol 218"), 
                    ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
                    ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
                    ("Jorge Russo", 15, 958, "Mirasol 218")
                ],  
                {"Calle Las Flores 355", "Mirasol 218", "La Mancha 761"}
            ),
        ]
    )
def test_multiple_tuples(clientes, expected):
    assert direccionesSinRepeticiones(clientes) == expected