def main():
    age = int(input('Input your age!: '))

    if age < 12:
        print ("You can't watch shrek 2, can't have a driving license, can't buy tobbaco products in Hungary and can't legally drink alcohol in America")
    elif age < 16:
        print ("You can watch shrek 2, but can't have a driving license, can't buy tobbaco products in Hungary and can't legally drink alcohol in America")
    elif age < 18:
        print ("You can watch shrek 2 and have a driving license, but can't buy tobbaco products in Hungary and can't legally drink alcohol in America")
    elif age < 21:
        print ("You can watch shrek 2, have a driving license and buy tobbaco products in Hungary, but can't legally drink alcohol in America")
    else:
        print ("You can watch shrek 2, have a driving license, also buy tobbaco products in Hungary and legally drink alcohol in America")

    
if __name__ == "__main__":
    main()