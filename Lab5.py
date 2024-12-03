import queue
from functools import reduce

graf = {
    (1, 1): [(1, 2), (1, 3), (1, 4), (2, 1), (3, 1), (4, 1)],
    (1, 2): [(1, 1), (1, 3), (1, 4), (2, 2), (3, 2), (4, 2)],
    (1, 3): [(1, 1), (1, 2), (1, 4), (2, 3), (3, 3), (4, 3)],
    (1, 4): [(1, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 4)],
    (2, 1): [(2, 2), (2, 3), (2, 4), (1, 1), (3, 1), (4, 1)],
    (2, 2): [(2, 1), (2, 3), (2, 4), (1, 2), (3, 2), (4, 2)],
    (2, 3): [(2, 1), (2, 2), (2, 4), (1, 3), (3, 3), (4, 3)],
    (2, 4): [(2, 1), (2, 2), (2, 3), (1, 4), (3, 4), (4, 4)],
    (3, 1): [(3, 2), (3, 3), (3, 4), (1, 1), (2, 1), (4, 1)],
    (3, 2): [(3, 1), (3, 3), (3, 4), (1, 2), (2, 2), (4, 2)],
    (3, 3): [(3, 1), (3, 2), (3, 4), (1, 3), (2, 3), (4, 3)],
    (3, 4): [(3, 1), (3, 2), (3, 3), (1, 4), (2, 4), (4, 4)],
    (4, 1): [(4, 2), (4, 3), (4, 4), (1, 1), (2, 1), (3, 1)],
    (4, 2): [(4, 1), (4, 3), (4, 4), (1, 2), (2, 2), (3, 2)],
    (4, 3): [(4, 1), (4, 2), (4, 4), (1, 3), (2, 3), (3, 3)],
    (4, 4): [(4, 1), (4, 2), (4, 3), (1, 4), (2, 4), (3, 4)],
}

domenVrednosti = {
    (1, 1): {1, 2, 3, 4},
    (1, 2): {1, 2, 3, 4},
    (1, 3): {1, 2, 3, 4},
    (1, 4): {1, 2, 3, 4},
    (2, 1): {1, 2, 3, 4},
    (2, 2): {1, 2, 3, 4},
    (2, 3): {1, 2, 3, 4},
    (2, 4): {1, 2, 3, 4},
    (3, 1): {1, 2, 3, 4},
    (3, 2): {1, 2, 3, 4},
    (3, 3): {1, 2, 3, 4},
    (3, 4): {1, 2, 3, 4},
    (4, 1): {1, 2, 3, 4},
    (4, 2): {1, 2, 3, 4},
    (4, 3): {1, 2, 3, 4},
    (4, 4): {1, 2, 3, 4},
}

def lcvAlgoritam(cvor: tuple, domen: dict, graf: dict, obr: set) -> int:
    trenDomen = domen[cvor]
    rez = dict()
    for el in trenDomen:
        br = 0
        for sused in graf[cvor]:
            if sused not in obr:
                if el in domen[sused]:
                    br += 1
        rez[el] = br
    return min(rez, key=rez.get)

def forwardChecking(cvor: tuple, domen: dict, graf: dict, vr: int, obr: set):
    for sused in graf[cvor]:
        if sused not in obr and vr in domen[sused]:
            domen[sused].remove(vr)

def formirajSudoku(g: dict, d: dict, start: tuple) -> dict:
    stek = queue.LifoQueue(len(g))
    obradjeni = set()
    setovani = set()
    rezultat = dict()
    stek.put(start)
    obradjeni.add(start)
    while not stek.empty():
        trenutniCvor = stek.get()
        najboljaOpcija = lcvAlgoritam(trenutniCvor, d, g, setovani)
        rezultat[trenutniCvor] = najboljaOpcija
        setovani.add(trenutniCvor)
        forwardChecking(trenutniCvor, d, g, najboljaOpcija, setovani)
        for sused in g[trenutniCvor]:
            if sused not in obradjeni and trenutniCvor[0] == sused[0]:
                stek.put(sused)
                obradjeni.add(sused)
    return rezultat

rezultat = dict()
rezultat.update(formirajSudoku(graf, domenVrednosti, (1, 1)))
rezultat.update(formirajSudoku(graf, domenVrednosti, (2, 1)))
rezultat.update(formirajSudoku(graf, domenVrednosti, (3, 1)))
rezultat.update(formirajSudoku(graf, domenVrednosti, (4, 1)))
print(rezultat)