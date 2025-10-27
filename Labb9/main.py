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


    try:

        q = LinkedQ()

        for char in input_str:
            q.enqueue(char)

        is_molecule(q)

        print("Formeln är syntaktiskt korrekt")

    except Syntaxfel as exception:
        print(exception.message, end=" ")
        while not q.isEmpty():
            print(q.dequeue(), end="")
        print()
        return False

    return True

def is_molecule(q):

    is_group(q)

    next = q.peek()

    if not q.isEmpty():
        is_molecule(q)

def handle_parnethesis(q):
    is_atom(q)
    is_num_or_empty(q)
    while True:
        next = q.peek()
        if next == None:
            raise Syntaxfel("Saknad högerparentes vid radslutet")
        if next not in "()":
            is_s_group(q)
        else:
            break
    next = q.peek()
    if next == "(":
        q.dequeue()
        handle_parnethesis(q)
    next = q.peek()
    if next ==")":
        q.dequeue()
        if not is_num(q):
            raise Syntaxfel("Saknad siffra vid radslutet")
        return
    elif next == None:
        raise Syntaxfel("Saknad högerparentes vid radslutet")
    else:
        raise Syntaxfel("Saknad högerparentes vid radslutet")

def is_num(q):
    next = q.peek()
    if next == None:
        raise Syntaxfel("Saknad siffra vid radslutet")
    if next == "0" or next == "1":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet")
    elif next in "23456789":
        parsed_string = ""
        while not q.isEmpty():
            next = q.peek()
            try:
                int(next)
                parsed_string += next
                q.dequeue()
            except:
                break
        return True
    return False


def is_s_group(q):
    is_atom(q)
    is_num_or_empty(q)


def is_group(q):

    next = q.peek()
    if next == "(":
        q.dequeue()
        handle_parnethesis(q)
    else:
        is_atom(q)
        is_num_or_empty(q)



    return True

def is_atom(q):

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

    elif is_lowercase_letter(chars):
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet")


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