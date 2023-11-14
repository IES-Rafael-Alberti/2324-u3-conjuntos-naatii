
crearConjunto:set = lambda lista: set(lista)
"""Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.

Args:
    lista: una lista cualquiera

Returns:
    set: Devuelve conjuntos a partir de las listas
"""

def encontrarFrutas(frutas1:set, frutas2:set)-> set:
    """Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.

    Args:
        frutas1 (set): lista de frutas que están en la lista 1
        frutas2 (set): lista de frutas que están en la lista 2

    Returns:
        set: diccionario con las frutas que están en la lista 1 y en la lista 2
    """
    frutasComunes = set(frutas1) & set(frutas2)
    return frutasComunes

def encontrarFrutasEnFrutas1PeroNoEnFrutas2(frutas1:set, frutas2:set)->set:
    """Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.

    Args:
        frutas1 (set): lista de frutas que están en la lista 1
        frutas2 (set): lista de frutas que están en la lista 2

    Returns:
        set: conjunto con las frutas que están en la lista 1 pero no en la lista 2
    """
    frutas_solo_en_frutas1 = frutas1 - frutas2
    return frutas_solo_en_frutas1
def encontrarFrutasEnFrutas2PeroNoEnFrutas1(frutas1:set, frutas2:set)->set:
    """Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.

    Args:
        frutas1 (set): lista de frutas que están en la lista 1
        frutas2 (set): lista de frutas que están en la lista 2

    Returns:
        set: conjunto con las frutas que están en la lista 1 pero no en la lista 2
    """
    frutas_solo_en_frutas2 = frutas2 - frutas1
    return frutas_solo_en_frutas2

def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1 = crearConjunto(frutas1)
    set_frutas2 = crearConjunto(frutas2)
    print(encontrarFrutas(set_frutas1, set_frutas2))
    print(encontrarFrutasEnFrutas1PeroNoEnFrutas2(set_frutas1, set_frutas2))
    print(encontrarFrutasEnFrutas2PeroNoEnFrutas1(set_frutas1, set_frutas2))

if __name__ == "__main__":
    main()