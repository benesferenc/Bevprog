def caesar(text):
    decode = ""
    for i in text:
        decode += chr(ord(i) - 3)
    return decode

def main():
    print(caesar("kwwsv=22|rxwx1eh2gTz7z<Zj[fT"))

if __name__ == "__main__":
    main()