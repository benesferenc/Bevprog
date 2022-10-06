from math import sqrt

def pitagorasz_t ():
    a = float(input("Adja meg az 'a' oldal: "))
    b = float(input("Adja meg a 'b' oldal: "))
    c = sqrt((a**2)+(b**2))

    print("Az atfogo merete: {}".format(c))

def sin_t ():
    b = int(input("Adja meg a 'b' oldalt: "))
    c = int(input("Adja meg a 'c' oldalt: "))
    sin_t = b/c

    print("Az eredmeny: {}".format (sin_t))

def cos_t ():
    a=int(input("add meg az 'a' oldalt: "))
    c=int(input("add meg a 'c' oldalt: "))
    cos_t=a/c
    print("Az eredmeny: {}".format (cos_t))


def main ():
    choice = int(input("Ha a pitagorasz tetelt valasztja, irjon 1-est. Ha a sinus tetelt, irjon 2-est. Ha a cosinus tetelt, irjon 3-ast: "))
    
    if choice == 1:
        pitagorasz_t ()
    elif choice == 2:
        sin_t ()
    elif choice == 3:
        cos_t ()
    else:
        print("Probalja meg ujra!")

if __name__ == "__main__":
    main()