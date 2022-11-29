def fgv(text, chars):
    txtback = ""
    for i in text:
        for j in chars:
            if i == j:
                txtback += i
    return txtback

def main():
    print(fgv("almaazjo2", "mj8232"))

if __name__ == "__main__":
    main()