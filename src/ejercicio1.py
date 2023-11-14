def direccionesSinRepeticiones(clientes:list)->set:
    direcciones = set()
    for items in range(len(clientes)):
        direcciones.add(clientes[items][-1])
    return direcciones

def main():
    clientes = [
                ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
                ("Jorge Russo", 7, 699, "Mirasol 218"), 
                ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
                ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
                ("Jorge Russo", 15, 958, "Mirasol 218")
            ]
    print(direccionesSinRepeticiones(clientes))

if __name__ == "__main__":
    main()