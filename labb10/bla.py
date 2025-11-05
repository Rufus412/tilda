atom = "hej)"

if atom[0] == "(":
    atom = atom[1:]
if atom[-1] == ")":
    atom = atom[:-1]

print (atom)