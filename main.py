import webbrowser
from random import randint

def beolvasas(cim, perc, ertekeles, melyikfajl):
    fr = open(melyikfajl, "r", encoding="UTF-8")
    sor = fr.readline().split(": ")
    while sor != [""]:
        cim.append(sor[0])
        perc.append(int(sor[1]))
        ertekeles.append(float(sor[2]))
        sor = fr.readline().split(": ")
    fr.close()

def menu():
    print("1. Netflix eredeti oldala")
    print("2. Az 5 legjobbra értékelt film")
    print("3. Top 5 leghosszabb film")
    print("4. Top 5 legrövidebb film")
    print("5. Egy random film ajánlása")
    print("6. A legrosszabb értékelést kapott film")
    print("7. Film hozzáadása")
    
    valasz = int(input("Mit szeretnél csinálni/megjeleníteni? (1 - 7):"))
    return valasz

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
    menu()
def top5leghosszabb(cim, perc, ertekeles):
    n = len(cim)
    for i in range(n):
        for j in range(n):
            if perc[i] > perc[j]:
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
        print(f"Film címe: {cim[z]} - Hossza: {perc[z]} perc\n")
    menu()



def top5legrovidebb(cim, perc, ertekeles):
    n = len(cim)
    for i in range(n):
        for j in range(n):
            if perc[i] < perc[j]:
                x = cim[i]
                y = perc[i]
                z = ertekeles[i]
                cim[i] = cim[j]
                perc[i] = perc[j]
                ertekeles[i] = ertekeles[j]
                cim[j] = x
                perc[j] = y
                ertekeles[j] = z  

    for z in range(5):
        print(f"Film címe: {cim[z]} - Hossza: {perc[z]}")   
    menu()

def randomfilm(cim):
    n = len(cim)
    r = randint(0, n)
    print()
    print(f"Random film: {cim[r]}")

    
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
    for z in range(5):
        print(f"Legrosszabbra értékelt film: {cim[z]} - Értékelése: {ertekeles[z]}")    

def bongeszo():
    webbrowser.open('https://netflix.com', new=2)

def iras(cim, perc, ertekeles, melyikfajl):
    fw = open(melyikfajl, "a", encoding="UTF-8")
    ujcim = input("Add meg az új film címét! ")
    ujperc = int(input("Add meg az új film hosszát percben(pl: 130)! "))
    ujertekeles = float(input("Add meg az új film értékelését(pl: 5.8)! "))
    cim.append(ujcim)
    perc.append(ujperc)
    ertekeles.append(ujertekeles)
    fw.write(f"{ujcim}: {ujperc}: {ujertekeles}\n")
    fw.close()

def main():
    cim = []
    perc = []
    ertekeles = []
    melyikfajl = ''
    valasz = menu()
    if valasz == 1:
        bongeszo()
    else:
        melyikfajl = melyikfajlkell()
        beolvasas(cim, perc, ertekeles, melyikfajl)
        if valasz == 2:
            legjobbfilmek(cim, perc, ertekeles)
        elif valasz == 3:
            top5leghosszabb(cim, perc, ertekeles)
        elif valasz == 4:
            top5legrovidebb(cim, perc, ertekeles)
        elif valasz == 5:
            randomfilm(cim)
        elif valasz == 6:
            legrosszabb(cim, ertekeles)
        elif valasz == 7:
            iras(cim, perc, ertekeles, melyikfajl)

main()