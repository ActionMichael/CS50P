def main():
    text = input("text: ")
    print(shorten(text))


def shorten(word):
    newtext = ""

    for i in range(len(word)):
    #如果"i"字元不是母音印出
        if word[i].lower() not in ["a", "e", "i", "o", "u"] :
            newtext += word[i]
    
    return newtext


if __name__ == "__main__":
    main()
