
from linkedQFile import *

class Syntaxfel(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def is_molecule(input_str):

    q = LinkedQ()

    for char in input_str:
        q.enqueue(char)

    try:

        is_atom(q)

        parsed_str = ""

        if q.peek() == "0":
            q.dequeue()
            raise Syntaxfel("För litet tal vid radslutet")

        while not q.isEmpty():
            parsed_str += q.dequeue()

        if not parsed_str == "":
            is_num(parsed_str)

        print("Formeln är syntaktiskt korrekt")

    except Syntaxfel as exception:
        print(exception.message, end=" ")
        while not q.isEmpty():
            print(q.dequeue(), end = "")
        print()
        return False

    return True


def is_atom(q):

    char = q.peek()

    if is_uppercase_letter(char):
        q.dequeue()
        next = q.peek()

        if next == None:
            return True

        if is_lowercase_letter(next):
            q.dequeue()
        else:
            try:
                int(next)
            except:
                raise Syntaxfel("Felaktig karaktär efter stor bokstav")
    else:
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet")
    return True

def is_uppercase_letter(char):
    return char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_lowercase_letter(char):
    return char in "abcdefghijklmnopqrstuvwxyz"

def is_num(parsed_str):
    try:
        if int(parsed_str) > 1:
            return True
        else:
            raise Syntaxfel("För litet tal vid radslutet")
    except ValueError:
        raise Syntaxfel("Är inte int")

if __name__=='__main__':
    while True:
        input_str = input()
        if input_str == "#":
            break
        else:
            is_molecule(input_str)