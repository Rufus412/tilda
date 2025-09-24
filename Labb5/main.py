from bintreeFile import *
from linkedQFile import *

# Alfabet för att iterera genom bokstäver senare i sök-algoritmen
alphabet = "abcdefghijklmnopqrstuvwxyzåäö"


# Trädobjekt för att lagra data om vilka ord vi ska kolla och har kollat
svenska = Bintree()
gamla = Bintree()
with open('word3.txt') as file:
    for line in file:
        svenska.put(line.strip())


def makechildren(parent, q):
    """
    Söker genom en nod och skapar barn till noden.

    Istället för retur manipulerar det objektet q
    return: none
    """

    # Lägger in ordet vi utgår från så att vi vet att vi hanterat det.
    gamla.put(parent.value)


    # Itererar och ändrar varje bokstav i ordet för att söka efter barn.
    for i in range(len(parent.value)):

        # Kopia av ordet
        word = list(parent.value)

        # BYter ut bokstaven på index i mot en annan bokstav
        for letter in alphabet.replace(word[i], ""):

            # Nu byter vi
            word[i] = letter

            # Nedan återskapar vi det nya ordet
            word_str = ""
            for l in word:
                word_str += l

            # Om ordet råkar vara det sökta slutordet är hela algoritmen klar
            if word_str == slutord:
                # Annonserar att det finns en väg
                print("Det finns en väg till", slutord)

                # Tömer kön så att ovanför i algoritmen bryts
                while not q.isEmpty():
                    q.dequeue()

                q.enqueue(Node(parent, slutord))


                last_node = q.dequeue()

                writechain(last_node)

                # Sätter in det sökta ordet så att vi vet att vi hittat det
                gamla.put(word_str)
                return

            # Om det nya ordet finns i svenska sparar vi det som ett barn
            if word_str in svenska:

                # Kollar om det inte är ett dumbarn
                if word_str not in gamla:

                    # Lägger in ordet i både kön och gamla ord.
                    q.enqueue(Node(parent, word_str))
                    gamla.put(word_str)

def writechain(node):
    if not node == None:
        writechain(node.parent)
        print(node.value)

# Kön som tillfälligt lagrar alla ord vi vill iterera genom
q = LinkedNodeQ()

# Ber om input från användaren, start och slut
startord = input("startord: ")
slutord = input("slutord: ")

# Lägger in startordet, så att vi sedan har den att utgå ifrån
starting_node = Node(None, startord)
q.enqueue(starting_node)

# Kollar om slutordet finns i listan
if slutord in svenska:

    # Breddenförstsökning
    while not q.isEmpty():
        word_node = q.dequeue()
        makechildren(word_node, q)

# När loopen är klar kollar vi om vi misslyckats hitta
if not slutord in gamla:
    print("Det finns ingen väg till ", slutord)