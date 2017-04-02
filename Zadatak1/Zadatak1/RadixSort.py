import math

def RadixSort(A):
    brojCifara = 10 
    maxDuzina = False  
    temp = -1
    pozicija = 1
    while not maxDuzina:
        maxDuzina = True
        liste = [list() for i in range(brojCifara)]
        for i in A:
            pom = i / pozicija
            liste[math.floor(pom % brojCifara)].append(i)
            if pom > 0:
                maxDuzina = False
        a = 0
        for b in range(brojCifara):
            lista = liste[b]
            for i in lista:
                A[a] = i
                a = a + 1
        pozicija = pozicija * brojCifara