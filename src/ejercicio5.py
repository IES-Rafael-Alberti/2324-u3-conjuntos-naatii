def paresDeUnConjunto(numeros:list)-> set:
    """Crea un conjunto pares que contenga los números pares del conjunto numeros.

    Args:
        numeros (list): lista de números

    Returns:
        set: conjunto con los números pares de la lista numeros
    """
    pares = set()
    for numero in numeros:
        if numero % 2 == 0:
            pares.add(numero)
    return pares

def conjuntoDeMultiplosDeTres(numeros:list)-> set:
    """Crea un conjunto que contenga los números multiplos de 3 del conjunto numeros.
    
    Args:
        numeros (list): lista de números

    Returns:
        set: conjunto con los números multiplos de 3 de la lista numeros
    """
    multiplos_de_3 = set()
    for numero in numeros:
        if numero % 3 == 0:
            multiplos_de_3.add(numero)
    return multiplos_de_3

def interseccionDeUnConjunto(conjunto:set, conjunto2:set)-> set:
    """Crea un conjunto que contenga los números que están en ambos conjuntos.

    Args:
        conjunto (set): conjunto de números
        conjunto2 (set): conjunto de números
        
    Returns:
        set: conjunto con los números que están en ambos conjuntos
    """
    interseccion = conjunto & conjunto2
    return interseccion

def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    conjunto1 = paresDeUnConjunto(numeros)
    conjunto2 = conjuntoDeMultiplosDeTres(numeros)
    print(conjunto1)
    print(conjunto2)
    print(interseccionDeUnConjunto(conjunto1, conjunto2))

if __name__ == "__main__":
    main()
