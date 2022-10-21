def main():
    print("Kérlek add meg a sorozatod hosszuságát (n egész szám)!")
    n = int(input("N értéke: "))
    
    elso = 0
    masodik = 1
    i = 0
    
    while i < n:
        sor = elso + masodik
        elso = masodik
        masodik = sor
        i += 1
        print(sor)
        
if __name__=="__main__":
    main()