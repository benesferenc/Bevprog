def main():
    
    Szam = int(input("Kérlek adj meg egy nullánál nagyobb egész számot! "))
    Forditott = 0
    Kovetkezo_szam = Szam

    while (Kovetkezo_szam > 0):
        Egyes_szamjegy = Kovetkezo_szam % 10
        Forditott = Forditott * 10 + Egyes_szamjegy
        Kovetkezo_szam = Kovetkezo_szam // 10 
        
    if Forditott == Szam:
        print("\n A beírt szám fordítottja = {0}".format(Forditott))
        print("\n A beírt szám tükörszám.")
    else:
        print("\n A beírt szám fordítottja = {0}".format(Forditott))
        print("\n A beírt szám nem tükörszám.")
    
if __name__ == "__main__":
    main()