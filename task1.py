import keyword


def decrypt_clue(text):
    '''Finds python keywords in a text.'''
    elist = []
    file = open(text, "r")
    read = file.read()
    ListOfWords = keyword.kwlist
    count = 0
    for word in ListOfWords:
        if word in read:
            elist.append(word)

    return (elist)


TheList = decrypt_clue(r"\Users\HardLand\Desktop\pythonn\mysterious.txt")
print(TheList)
