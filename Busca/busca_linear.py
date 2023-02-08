def busca_linear(lista, item):
    for i in range(0, len(lista)):
        if lista[i] == item:
            return i
    return None
