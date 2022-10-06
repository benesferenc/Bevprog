import math

def kor_terulet(r):
    kor_terulet = r**2*math.pi
    return kor_terulet

def teglalap_terulet(a,b):
    teglalap_terulet = a*b
    return teglalap_terulet

def gula_terfogat(a,b,mg):
    gula_terfogat = teglalap_terulet(a,b)*mg/3
    return gula_terfogat

def kup_terfogat(r,mk):
    kup_terfogat = kor_terulet(r)*mk/3
    return kup_terfogat

def main():

    a = int(input('Adja meg a teglalap "a" oldalat: '))
    b = int(input('Adja meg a teglalap "b" oldalat: '))
    r = int(input('Adja meg a kor sugarat: '))
    which = int(input('Ha a gula terfogatat szeretné irjon 1-est, ha a kupet irjon 2-est: '))

    if which == 1:
        mg = int(input('Adja meg a gula magassagat: '))
        print('\nA gula terfogata: {0}'.format(gula_terfogat(a,b,mg)))
    elif which == 2:
        mk = int(input('Adja meg a kup magassagat: '))
        print('A kup terfogata: {0}\n'.format(kup_terfogat(r,mk)))
    else:
        print('Rossz számot adott meg!')

if __name__ == "__main__":
    main()