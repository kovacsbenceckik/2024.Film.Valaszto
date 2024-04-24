import webbrowser
from random import randint

def beolvasas(cim, perc, ertekeles, melyikadat):
    fr = open(melyikadat, "r", encoding="UTF-8")
    sor = fr.readline().split(": ")
    while sor != [""]:
        cim.append(sor[0])
        perc.append(int(sor[1]))
        ertekeles.append(float(sor[2]))
        sor = fr.readline().split(": ")

def menu():
    print("1. Adjá pézt :)")
    print("2. Az 5 legjobbra értékelt film")
    print("3. Top 5 leghosszabb film")
    print("4. Top 5 legrövidebb film")
    print("5. Egy random film ajánlása")
    print("6. A legrosszabb értékelést kapott film")
    
    valasz = int(input("Milyen filmeket szeretnél kapni? (1 - 6):"))
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
    
def randomfilm(cim):
    n = len(cim)
    r = randint(0, n)

    
def legrosszabb(cim, ertekeles):
    legk = 0
    for i in range(1, len(ertekeles)):
        if ertekeles[i] < ertekeles[legk]:
            legk = i
    return cim[legk]


def bongeszo():
    webbrowser.open('https://www.paypal.com/paypalme/benro213', new=2)

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
    # print(melyikfajl)
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
            legrosszabb()

main()