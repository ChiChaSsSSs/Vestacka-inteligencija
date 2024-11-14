from itertools import zip_longest
from functools import reduce

# Zadatak 1
def poredak(lista1: list[int], lista2: list[int]) -> list[tuple[int, int, str]]:
    return list(map(lambda x: (x[0], x[1], "Jeste" if x[1] == 2 * x[0] else "Nije"), list(zip_longest(lista1, lista2, fillvalue=0))))

# Zadatak 2
def spojidict(lista1: list[object], lista2: list[object]) -> list[dict[str, object]]:
    return list(map(lambda x: dict({"prvi" : x[0], "drugi" : x[1]}), list(zip_longest(lista1, lista2, fillvalue="-"))))
    
# Zadatak 3
def spoji(lista1: list[int], lista2: list[int]) -> list[tuple[int, int, int]]:
    return list(map(lambda x: (min(x[0], x[1]), max(x[0], x[1]), x[0] + x[1]), list(zip_longest(lista1, lista2, fillvalue=0))))
    
# Zadatak 4
def suma(lista: list[object]) -> int:
    return reduce(lambda x, y: x + y, [z for z in [reduce(lambda p, q: p + q, r, 0) for r in lista]], 0)

# Zadatak 5
def proizvod(lista1: list[list], lista2: list[int]) -> list[int]:
    return list(map(lambda x: x[0] *  x[1], list(zip_longest(list(map(lambda x: x[0] + x[1] + x[2], lista1)), lista2, fillvalue=0))))
    
# Zadatak 6
def objedini(lista1: list[int], lista2: list[int]) -> list[tuple[int, int]]:
    return list(map(lambda x: (min(x[0], x[1]), max(x[0], x[1])), list(zip_longest(lista1, lista2, fillvalue=0))))

# Zadatak 7
def objedini2(lista: list[tuple]) -> dict[object, object]:
    return dict(reduce(lambda acc, el: acc | {el[0]: el[1:] if el[1:] else None}, lista, dict()))

# Zadatak 8
def izracunaj(lista: list[object]) -> list[int]:
    return list(map(lambda x: x if isinstance(x, int) else int((reduce(lambda acc, br: acc * br, x, 1))), lista))

# Zadatak 9
def zamena(lista: list[int], broj: int) -> list[int]:
    return list(map(lambda x: x[1] if x[1] >= broj else (reduce(lambda acc, el: acc + el, lista[x[0] + 1:], 0)), enumerate(lista)))
    
# Zadatak 10
def stepen(lista: list[int]) -> list[int]:
    return list(map(lambda x, y: x**y, lista, lista[1:]))    
    
# Zadatak 11
def proizvod2(lista: list[list[int]]) -> int:
    return reduce(lambda acc1, el1: acc1 * el1, [x for x in [reduce(lambda acc2, el2: acc2 * el2, l, 1) for l in lista]], 1)
    
# Zadatak 12
def izracunaj2(lista: list[object]) -> list[int]:
    return list(map(lambda x: x**2 if isinstance(x, int) else (reduce(lambda acc, br: acc + br**2, x, 0)), lista))    
    
# Zadatak 13
def skupi(lista: list[list[int]]) -> list[list[int]]:
    return [[br[0] + br[1] for br in zip_longest(x, y, fillvalue=0)] for x, y in zip(lista, lista[1:])]

# Zadatak 14
def suma2(lista: list[list[int]]) -> int:
    return reduce(lambda acc1, el1: acc1 + el1, [x for x in[reduce(lambda acc2, el2: acc2 * el2, l, 1) for l in lista]], 0)

print(poredak([1, 7, 2, 4], [2, 5, 2]))
print(spojidict([1, 7, 2, 4], [2, 5, 2]))
print(spoji([1, 7, 2, 4], [2, 5, 2]))
print(suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]))
print(objedini([1, 7, 2, 4, 5], [2, 5, 2]))
print(objedini2([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]))
print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))
print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))
print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))
print(proizvod2([[1, 3, 5], [2, 4, 6], [1, 2, 3]]))
print(izracunaj2([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))
print(skupi([[1, 3, 5], [2, 4, 6], [1, 2]]))
print(suma2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))