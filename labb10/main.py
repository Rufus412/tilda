from linkedQFile import *
from molgrafik import *


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


Atoms_string = ("""H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V  
 Cr Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv""")

def skapaAtomDict():
    """Skapar och returnerar en lista med Atom-objekt"""
    atomdata = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"

    atomdict = {}
    lista = atomdata.split(";")
    for namn_vikt in lista:
        namn, vikt = namn_vikt.split()

        atomdict[namn] = float(vikt)
    return atomdict

Atom_weights = skapaAtomDict()

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


def weight(mol: Ruta):

    atom_name = mol.atom
    if atom_name == "( )":
        w = weight(mol.down) * mol.num
    else:
        w = Atom_weights[atom_name] * mol.num

    if mol.next:
        w += weight(mol.next)

    return w



class Syntaxfel(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def start(formel):

    q = LinkedQ()

    for char in formel:
        q.enqueue(char)

    mg = Molgrafik()

    try:

        mol = readformel(q)

        w = weight(mol)

        print("Molekylen väger:", w)

        mg.show(mol)

    except Syntaxfel as exception:
        print(exception.message, end="")

        if not q.isEmpty():
            print(" ", end="")
        while not q.isEmpty():
            print(q.dequeue(), end="")
        print()

def readformel(q):

    mol = readmol(q)

    if q.peek() != None and q.peek() == ")":
        raise Syntaxfel("Felaktig gruppstart vid radslutet")

    return mol


def readmol(q):

    mol = readgroup(q)

    if q.peek() != None and q.peek() != ")":

        mol.next = readmol(q)

    return mol

def readgroup(q):

    rutan = Ruta()

    if q.peek() != None and q.peek() == "(":

        q.dequeue()

        rutan.down = readmol(q)

        if q.peek() != None and q.peek() == ")":
            q.dequeue()
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet")

        rutan.num = readnumber(q)
    elif q.peek() not in LETTER:
        if q.peek() in letter:
            raise Syntaxfel("Saknad stor bokstav vid radslutet")
        else:
            raise Syntaxfel("Felaktig gruppstart vid radslutet")
    else:

        rutan.atom = readatom(q)

        if q.peek() != None and q.peek() in numbers:

            rutan.num = readnumber(q)

    return rutan


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

    return atom_str




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

    return int(nr_string)



if __name__=='__main__':

    while True:
        formel = input("Molekyl: ")
        if formel == "#":
            break
        else:
            start(formel)
