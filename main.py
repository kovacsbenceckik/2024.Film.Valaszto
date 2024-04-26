from random import randint
from time import sleep

def beolvasas(cim, perc, ertekeles, melyikfajl, osszeg):
    fr = open(melyikfajl, "r", encoding="UTF-8")
    sor = fr.readline().split(": ")
    while sor != [""]:
        cim.append(sor[0])
        perc.append(int(sor[1]))
        ertekeles.append(float(sor[2]))
        sor = fr.readline().split(": ")
        osszeg += 1
    fr.close()
    print()
    print(f"Ez a fájl {osszeg} film adatát tartalmazza\nBetöltés...")
    sleep(0.5)

def menu(cim, perc, ertekeles, melyikfajl):
    print("1. Az 5 legjobbra értékelt film")
    print("2. Top 5 leghosszabb film")
    print("3. Top 5 legrövidebb film")
    print("4. Egy random film ajánlása")
    print("5. A legrosszabb értékelést kapott film")
    print("6. Film hozzáadása")
    print("7. 3 óránál hosszabb filmek")
    print("8. Címkeresés első karakter megadásával")
    
    valasz = int(input("Mit szeretnél csinálni/megjeleníteni? (1 - 8):"))
    if valasz == 1:
        legjobbfilmek(cim, perc, ertekeles)
    elif valasz == 2:
        top5leghosszabb(cim, perc)
    elif valasz == 3:
        top5legrovidebb(cim, perc)
    elif valasz == 4:
        randomfilm(cim)
    elif valasz == 5:
        legrosszabb(cim, ertekeles)
    elif valasz == 6:
        iras(cim, perc, ertekeles, melyikfajl)
    elif valasz == 7:
        cimek = haromoranaltobb(cim, perc)
        print("3 óránál hosszabb filmek:")
        for i in range(len(cimek)):
            print()
            print(f"{cimek[i]}")
    elif valasz == 8:
        karakter = input("Melyik karakterrel kezdődő filmeket keresel? ")
        karakter = karakter.upper()
        kereses(cim, perc, ertekeles, karakter, melyikfajl)
    else:
        print()
        print("Nincs ilyen menüpont.")
        print()
        menu(cim, perc, ertekeles, melyikfajl)

def melyikfajlkell():
    melyikfajl = input("Melyik fájlból szeretnéd ezt végrehajtani? (Fájlnévkiterjesztéssel!) ")

    return melyikfajl
    
def legjobbfilmek(cim, perc, ertekeles):
    n = len(cim)
    for i in range(n):
        for j in range(n):
            if ertekeles[i] > ertekeles[j]:
                x = cim[i]
                y = perc[i]
                z = ertekeles[i]
                cim[i] = cim[j]
                perc[i] = perc[j]
                ertekeles[i] = ertekeles[j]
                cim[j] = x
                perc[j] = y
                ertekeles[j] = z 
    print()       
    for z in range(5):
        print(f"Film címe: {cim[z]} - Értékelése: {ertekeles[z]}\n")

def top5leghosszabb(cim, perc):
    n = len(cim)
    for i in range(n):
        for j in range(n):
            if perc[i] > perc[j]:
                x = cim[i]
                y = perc[i]
                cim[i] = cim[j]
                perc[i] = perc[j]
                cim[j] = x
                perc[j] = y
    print()
    for z in range(5):
        print(f"Film címe: {cim[z]} - Hossza: {perc[z]} perc\n")



def top5legrovidebb(cim, perc):
    n = len(cim)
    for i in range(n):
        for j in range(n):
            if perc[i] < perc[j]:
                x = cim[i]
                y = perc[i]
                cim[i] = cim[j]
                perc[i] = perc[j]
                cim[j] = x
                perc[j] = y

    for z in range(5):
        print(f"Film címe: {cim[z]} - Hossza: {perc[z]}")   

def randomfilm(cim):
    n = len(cim)
    r = randint(0, n)
    print()
    print(f"Random film: {cim[r]}\n")

    
def legrosszabb(cim, ertekeles):
    n = len(cim)
    for i in range(n):
        for j in range(n):
            if ertekeles[i] < ertekeles[j]:
                x = cim[i]
                z = ertekeles[i]
                cim[i] = cim[j]
                ertekeles[i] = ertekeles[j]
                cim[j] = x
                ertekeles[j] = z 
    print()
    print(f"Legrosszabbra értékelt film: {cim[0]} - Értékelése: {ertekeles[0]}")    

def bennevan(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)

def iras(cim, perc, ertekeles, melyikfajl):
    fw = open(melyikfajl, "a", encoding="UTF-8")
    ujcim = input("Add meg az új film címét! ")
    if not bennevan(ujcim, cim):
        ujperc = int(input("Add meg az új film hosszát percben(pl: 130)! "))
        ujertekeles = float(input("Add meg az új film értékelését 0.0-10.0-ig(pl: 5.8)! "))
        if ujertekeles < 0:
            print("A megadott tartományban add meg az értékelést!")
        else:
            cim.append(ujcim)
            perc.append(ujperc)
            ertekeles.append(ujertekeles)
            fw.write(f"{ujcim}: {ujperc}: {ujertekeles}\n")
    else:
        print("Ez a film már benne van a fájlban.")
    fw.close()

def haromoranaltobb(cim, perc):
    cimek = []
    for i in range(len(cim)):
        if perc[i] >= 180:
            cimek.append(cim[i])
    return cimek

def kereses(cim, perc, ertekeles, karakter, melyikfajl):
    n = len(cim)
    for i in range(n):
        if len(karakter) == 1 and cim[i][0] == karakter:
            print(cim[i])
            print()
    menu(cim, perc, ertekeles, melyikfajl)

def main():
    cim = []
    perc = []
    ertekeles = []
    osszeg = 0
    melyikfajl = melyikfajlkell()
    beolvasas(cim, perc, ertekeles, melyikfajl, osszeg)
    menu(cim, perc, ertekeles,melyikfajl)

main()