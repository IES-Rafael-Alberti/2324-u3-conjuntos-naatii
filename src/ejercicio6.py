def crearSubconjunto(vocales:set, consonantes:set)->set:
    return vocales.union(consonantes)

def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r','s', 't', 'v', 'w', 'x', 'y', 'z'}
    print(crearSubconjunto(vocales, consonantes))

if __name__ == '__main__':
    main()