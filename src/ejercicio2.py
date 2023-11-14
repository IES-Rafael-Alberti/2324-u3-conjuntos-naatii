def todosLosAlumnos(alumnoPrimaria:set, alumnoSecundaria:set)->set:
    return alumnoPrimaria.union(alumnoSecundaria)

def alumnosRepetidos(alumnoPrimaria:set, alumnoSecundaria:set)->set:
    return alumnoPrimaria.intersection(alumnoSecundaria)

def alumnosNoRepetidos(alumnoPrimaria:set, alumnoSecundaria:str)->set:
    return alumnoPrimaria.difference(alumnoSecundaria)

def alumnosPrimariaIncluidosEnSecundaria(alumnoPrimaria:set, alumnoSecundaria:set)->set:
    return alumnoPrimaria.issubset(alumnoSecundaria)

def mensajeSalida(alumnoPrimaria:set, alumnoSecundaria:set)->str:
    print(f"\nLa lista de todos los alumnos son: {todosLosAlumnos(alumnoPrimaria, alumnoSecundaria)}\n")
    print(f"La lista de todos los alumnos de primaria repetidos en secundaria son: {alumnosRepetidos(alumnoPrimaria, alumnoSecundaria)}\n")
    print(f"La lista de todos los alumnos de primaria no repetidos en secundaria son: {alumnosNoRepetidos(alumnoPrimaria, alumnoSecundaria)}\n")
    if alumnosPrimariaIncluidosEnSecundaria(alumnoPrimaria, alumnoSecundaria) == True:
        print(f"La lista de todos los alumnos incluidos en la secundaria son: {alumnoPrimaria}\n")
    else:
        print("no están todos alumnos de primaria incluidos en la secundaria\n")

def main():
    salida = "x"
    alumnoPrimaria = set()
    alumnoSecundaria = set()
    alumno = ""
    while alumno.lower() != salida:
        alumno = input("ingrese el nombre del alumno de primaria: ")
        if alumno != "x":
            alumnoPrimaria.add(alumno)
    alumno = ""
    while alumno.lower()!= salida:
        alumno = input("ingrese el nombre del alumno de secundaria: ")
        if alumno != "x":
            alumnoSecundaria.add(alumno)
    mensajeSalida(alumnoPrimaria, alumnoSecundaria)
    print("chaaaaaao chao chao chao")
if __name__ == "__main__":
    main()