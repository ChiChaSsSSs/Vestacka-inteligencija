def numlista(lista: list) -> dict:
    tipovi = set(map(lambda x: (type(x).__name__), lista))
    recnik = {t: [] for t in tipovi}
    for x in lista:
        recnik[type(x).__name__].append(x)
    return recnik

print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))