def direccionesSinRepeticiones(clientes:list)->set:
    """crea un diccionario con las direcciones de los clientes.

    Args:
        clientes (list): es la lista de tuplas con los datos del cliente

    Returns:
        set: el diccionario con las direcciones de los clientes
    """
    direcciones = set()
    for items in range(len(clientes)):
        direcciones.add(clientes[items][-1])
    return direcciones

def main():
    """Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:

    [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    """
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