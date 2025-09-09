from bintreeFile import *

svenska = Bintree()
gamla = Bintree()
with open('words.txt') as file:
    for line in file:
        svenska.put(line.strip())


