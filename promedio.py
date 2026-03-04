def promedio(lista):
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista.")

    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")

    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos deben ser números.")

    return sum(lista) / len(lista)
