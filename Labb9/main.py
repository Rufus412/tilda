from os import WCONTINUED
from traceback import print_stack

from linkedQFile import *

Atoms_string = ("""H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V  
 Cr Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv""")

Atoms = Atoms_string.split()



class Syntaxfel(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def start(input_str):

    p_stack = []

    try:

        q = LinkedQ()

        for char in input_str:
            q.enqueue(char)

        is_molecule(q, p_stack)

        print("Formeln är syntaktiskt korrekt")

    except Syntaxfel as exception:
        print(exception.message, end=" ")
        while not q.isEmpty():
            print(q.dequeue(), end="")
        print()
        return False

    return True

def is_molecule(q, p_stack):

    is_group(q, p_stack)

    if not q.isEmpty():
        is_molecule(q, p_stack)


def is_group(q, p_stack):

    next = q.peek()

    if next == None:
        return True

    if next in "()":
        if next == "(":
            p_stack.append("(")
        elif p_stack[-1] == "(":
            p_stack.pop()

        q.dequeue()
        is_molecule(q, p_stack)

        is_num_or_empty(q)

    else:
        is_atom(q, p_stack)

        is_num_or_empty(q)

    return True

def is_atom(q, p_stack):

    chars = q.peek()

    if is_uppercase_letter(chars):
        q.dequeue()
        next = q.peek()

        if next == None:
            return True

        if is_lowercase_letter(next):
            chars += next
            q.dequeue()
        return is_in_Atoms(chars)
    elif chars == ")" and p_stack[-1] == "(":
        return True
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

def is_in_Atoms(chars):
    if chars in Atoms:
        return True
    else:
        raise Syntaxfel("Okänd atom vid radslutet")

def is_uppercase_letter(char):
    return char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_lowercase_letter(char):
    return char in "abcdefghijklmnopqrstuvwxyz"

def is_num_or_empty(q):
    next = q.peek()

    if next == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet")

    parsed_string = ""

    while True:
        try:
            int(next)
            parsed_string += next
            q.dequeue()
            next = q.peek()
        except:
            break

    if parsed_string == "1":
        raise Syntaxfel("För litet tal vid radslutet")


if __name__=='__main__':
    while True:
        input_str = input()
        if input_str == "#":
            break
        else:
            start(input_str)