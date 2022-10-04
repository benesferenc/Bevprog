def main():
    Sodium = int(input("Input a number of Sodium:"))
    Chlorine = int(input("Input a number of Chlorine:"))
    NaCl = 0
    excessSodium = 0
    excessChlorine = 0

    if Sodium < 2:
        excessSodium = Sodium
        excessChlorine = Chlorine
    elif Sodium == Chlorine * 2:
        NaCl = Sodium
    elif Sodium > Chlorine *2:
        NaCl = Chlorine * 2
        excessSodium = Sodium - Chlorine * 2
    elif Sodium % 2 == 1 < Chlorine:
        NaCl = Sodium - 1
        excessSodium = 1
        excessChlorine = Chlorine - Sodium
    elif Sodium < Chlorine:
        NaCl = Sodium
        excessChlorine = Chlorine - Sodium
    elif Sodium % 2 == 1:
        NaCl = Sodium - 1
        excessSodium = 1
        excessChlorine = Chlorine - (Sodium - 1) / 2
    else:
        NaCl = Sodium
        excessChlorine = Chlorine - Sodium / 2

    print("Created NaCl: {0},\nExcess Sodium: {1},\nExcess Chlorine: {2}".format(NaCl, excessSodium, excessChlorine))

if __name__ == "__main__":
    main()