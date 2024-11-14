import queue

# Zadatak 17

graf = {
    'A': ([('B', 5), ('D', 9), ('F', 4)]),
    'B': ([('A', 5), ('E', 9)]),
    'C': ([('D', 2), ('F', 4), ('G', 2), ('H', 3)]),
    'D': ([('A', 9), ('C', 2), ('E', 7)]),
    'E': ([('B', 9), ('I', 1)]),
    'F': ([('A', 4), ('C', 4), ('H', 8)]),
    'G': ([('C', 2)]),
    'H': ([('C', 3), ('F', 8)]),
    'I': ([('E', 1)])
}

def formHeuristic(g: dict, cvor: str) -> dict:
    redCvorova = queue.Queue(len(g))
    redCvorova.put(cvor)
    heuristika = dict()
    heuristika[cvor] = 0
    obidjeni = set()
    obidjeni.add(cvor)
    
    while not redCvorova.empty():
        trenutni = redCvorova.get()
        
        for dest in g[trenutni]:
            if dest[0] not in obidjeni:
                heuristika[dest[0]] = heuristika[trenutni] + dest[1]
                obidjeni.add(dest[0])
                redCvorova.put(dest[0])
            else:
                if heuristika[dest[0]] > heuristika[trenutni] + dest[1]:
                    heuristika[dest[0]] = heuristika[trenutni] + dest[1]
    
    for dest in heuristika:
        g[dest] = (g[dest], heuristika[dest])
        
    return g
                
print(formHeuristic(graf, 'A'))