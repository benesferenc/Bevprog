def findfgv():
    text = "Az egy bögre"
    ftext = "piros"
    ujtext = ""
    for i in range(len(text)):
        if i == 6 and text.find("bögre"):
            ujtext += text.replace("bögre", ftext + " bögre")
    print(ujtext)
    
def main():
    findfgv()
     
if __name__=="__main__":
    main()