import webbrowser

def menu():
    print("1. Az 5 legjobbra értékelt film")
    print("2. Top 5 leghosszabb film")
    print("3. Top 5 legrövidebb film")
    print("4. Egy random film ajánlása")
    print("5. A legrosszabb értékelést kapott film")
    print("6. Adjá pézt")
    
    valasz = input("Milyen filmeket szeretnél kapni? (1 - 6):")
    
    # if valasz == 1:
    #     legjobbfilmek()
    # elif valasz == 2:
    #     top5leghosszabb()
    # elif valasz == 3:
    #     top5legrovidebb()
    # elif valasz == 4:
    #     randomfilm()
    # elif valasz == 5:
    #     legrosszabb()
    # elif valasz == 6:
    #     bongeszo()
        
def bongeszo():
    webbrowser.open('https://youtube.com', new=2)        

def main():
    # valasz = menu()
    bongeszo()
main()