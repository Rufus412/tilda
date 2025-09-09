from bintreeFile import *
from linkedQFile import *

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

svenska = Bintree()
gamla = Bintree()
with open('word3.txt') as file:
    for line in file:
        svenska.put(line.strip())


def makechildren(starting_word, q):
    """
    skapar barn till noderna
    """

    gamla.put(starting_word)

    print(starting_word)

    for i in range(len(starting_word)):
        word = list(starting_word)
        for letter2 in alphabet.replace(word[i], ""):
            word[i] = letter2

            word_str = ""
            for l in word:
                word_str += l


            if word_str == slutord:
                print("Det finns en väg till", slutord)
                while not q.isEmpty():
                    q.dequeue()
                gamla.put(word_str)
                return

            if word_str in svenska:
                if word_str not in gamla:
                    q.enqueue(word_str)
                    gamla.put(word_str)

q = LinkedQ()

startord = input("startord: ")
slutord = input("slutord: ")

q.enqueue(startord)

while not q.isEmpty():
    word = q.dequeue()
    makechildren(word, q)

if not slutord in gamla:
    print("Det finns ingen väg till ", slutord)

gamla.write()