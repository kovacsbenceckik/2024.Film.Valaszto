import webbrowser

def beolvasas(cim, perc, ertekeles, melyikadat):
    fr = open(melyikadat, "r", encoding="UTF-8")
    sor = fr.readline().split(": ")
    while sor != [""]:
        cim.append(sor[0])
        perc.append(int(sor[1]))
        ertekeles.append(float(sor[2]))
        sor = fr.readline().split(": ")
    print(cim)
    print(perc)
    print(ertekeles)

def menu():
    print("1. Az 5 legjobbra értékelt film")
    print("2. Top 5 leghosszabb film")
    print("3. Top 5 legrövidebb film")
    print("4. Egy random film ajánlása")
    print("5. A legrosszabb értékelést kapott film")
    print("6. Adjá pézt :)")
    
    valasz = input("Milyen filmeket szeretnél kapni? (1 - 6):")
    return valasz

def melyikfajlkell():
    melyikfajl = input("Melyik fájlból szeretnéd ezt végrehajtani? (Fájlnévkiterjesztéssel!) ")
    return melyikfajl
    
# def legjobbfilmek():
     
        
        
# def top5leghosszabb():



# def top5legrovidebb():
    
    
    
# def randomfilm():
    
    
    
# def legrosszabb():
    


# def bongeszo():
#     webbrowser.open('https://www.paypal.com/paypalme/benro213', new=2)

def main():
    cim = []
    perc = []
    ertekeles = []
    melyikfajl = ''
    valasz = menu()
    if valasz == 6:
        pass
    else:
        melyikfajl = melyikfajlkell()
    # print(melyikfajl)
        beolvasas(cim, perc, ertekeles, melyikfajl)
        # if valasz == 1:
            #legjobbfilmek()
        # elif valasz == 2:
        #     top5leghosszabb()
        # elif valasz == 3:
        #     top5legrovidebb()
        # elif valasz == 4:
        #     randomfilm()
        # elif valasz == 5:
        #     legrosszabb()
main()