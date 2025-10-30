from linkedQFile import *

Atoms_string = ("""H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V  
 Cr Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv""")


"""
<formel>::= <mol>
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
"""

Atoms = Atoms_string.split()

LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = LETTER.lower()

numbers = "0123456789"


class Syntaxfel(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def start(formel):

    q = LinkedQ()

    for char in formel:
        q.enqueue(char)

    try:

        readformel(q)

        print("Formeln är syntaktiskt korrekt ")

    except Syntaxfel as exception:
        print(exception.message, end="")

        if not q.isEmpty():
            print(" ", end="")
        while not q.isEmpty():
            print(q.dequeue(), end="")
        print()

def readformel(q):

    readmol(q)

    if q.peek() != None and q.peek() == ")":
        raise Syntaxfel("Felaktig gruppstart vid radslutet")


def readmol(q):

    readgroup(q)

    if q.peek() != None and q.peek() != ")":

        readmol(q)

def readgroup(q):

    if q.peek() != None and q.peek() == "(":

        q.dequeue()

        readmol(q)

        if q.peek() != None and q.peek() == ")":
            q.dequeue()
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet")

        readnumber(q)
    elif q.peek() not in LETTER:
        if q.peek() in letter:
            raise Syntaxfel("Saknad stor bokstav vid radslutet")
        else:
            raise Syntaxfel("Felaktig gruppstart vid radslutet")
    else:

        readatom(q)

        if q.peek() != None and q.peek() in numbers:

            readnumber(q)


def readatom(q):

    atom_str = ""

    if q.peek() != None and q.peek() in LETTER:
        atom_str += q.dequeue()

        if q.peek() != None and q.peek() in letter:
            atom_str += q.dequeue()
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    if not atom_str in Atoms:
        raise Syntaxfel("Okänd atom vid radslutet")




def readnumber(q):
    nr_string = ""

    if q.peek() == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet")

    while q.peek() != None and q.peek() in numbers:
        nr_string += q.dequeue()

    if nr_string == '':
        raise Syntaxfel("Saknad siffra vid radslutet")

    if int(nr_string) == 1:
        raise Syntaxfel("För litet tal vid radslutet")




if __name__=='__main__':

    while True:
        formel = input()
        if formel == "#":
            break
        else:
            start(formel)