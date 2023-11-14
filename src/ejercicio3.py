def todosLosSubconjuntos(conjunto):
    conjunto = list(conjunto)
    n = len(conjunto)
    todos_los_subconjuntos = [[]]

    for i in range(n):
        for j in range(len(todos_los_subconjuntos)):
            todos_los_subconjuntos.append(todos_los_subconjuntos[j] + [conjunto[i]])

    return [set(subconjunto) for subconjunto in todos_los_subconjuntos]

if __name__ == "__main__":
    print(todosLosSubconjuntos({1, 2, 3}))
    print(todosLosSubconjuntos({"a", "b", "c"}))
    print(todosLosSubconjuntos({4, 3, 2, 6}))
