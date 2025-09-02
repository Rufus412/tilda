from bintreeFile import Bintree

svenska = Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        svenska.put(ordet)             # in i sökträdet


engelska = Bintree()

with open("engelska.txt", "r", encoding = "utf-8") as engelskafil:

    content = engelskafil.readlines()

    lines = [line.strip().split() for line in content]
    words = []
    for line in lines:
        words.extend(line)

    for word in words:
         engelska.put(word.strip('\",!.'))

for word in engelska:
    if word in svenska:
        print (word)