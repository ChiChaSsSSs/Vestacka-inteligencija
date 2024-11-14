from functools import reduce

# Zadatak 1
def parni(lista: list[int]) -> dict:
    parniBrojevi = list(filter(lambda x: x % 2 == 0, lista))
    neparniBrojevi = list(filter(lambda x: x % 2 != 0, lista))
    recnik = {
        "Jeste": [],
        "Nije": []
    }
    recnik["Jeste"] = parniBrojevi
    recnik["Nije"] = neparniBrojevi
    return recnik

# Zadatak 2  
def numlista(lista: list) -> dict:
    tipovi = set(map(lambda x: (type(x).__name__), lista))
    recnik = {t: [] for t in tipovi}
    for x in lista:
        recnik[type(x).__name__].append(x)
    return recnik

# Zadatak 3
def uredi(lista: list[int], brojElemenata: int, korekcija: int) -> list[int]:
    return list(map(lambda x: x[1] + korekcija if x[0] < brojElemenata else x[1] - korekcija, enumerate(lista)))

# Zadatak 4
def zbir(lista: list[int]) -> list[int]:
    return [lista[i] + lista[i + 1] for i in range(0, len(lista) - 1)]

# Zadatak 5
def brojel(lista: list) -> list[int]:
    return [len(x) if type(x).__name__ == 'list' else -1 for x in lista]

# Zadatak 6
def razlika(lista1: list, lista2: list) -> list:
    return list(filter(lambda el: el != None, [x if x in lista2 else None for x in lista1]))

# Zadatak 7
def saberi(lista: list[tuple]) -> list[int]:
    rezultat = []
    for el in lista:
      rezultat.append(reduce(lambda x, y: x + y, el))
    return rezultat
    
# Zadatak 8
def izmeni(lista: list[int]) -> list[int]:
    rezultat = []
    for i in range(0, len(lista)):
        rezultat.append(reduce(lambda x, y: x + y, lista[: i + 1]))
    return rezultat

# Zadatak 9
def prosek(lista: list[list]) -> list[float]:
    rezultat = []
    for podlista in lista:
        rezultat.append((reduce(lambda x, y: x + y, podlista) / len(podlista)))
    return rezultat
  
print(parni([1,2,3,4,5,6,7,8,9]))
print(numlista(["String", 10, 8.13, [1,2,3], "DrugiString", 5]))
print(uredi([1, 2, 3, 4, 5], 3, 1))
print(zbir([1,2,3,4,5]))
print(brojel([[1,2,3,"5","6"], [1,2,3], "EL", ["X","y"]]))
print(razlika(["Prvi", 2, 3, "Cetiri", "Pet"] ,["Marko", 1, 2, "Pet"]))
print(saberi([(1, 4, 6), (2, 4), (4, 1)]))
print(izmeni([1,2,4,7,9]))
print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))


