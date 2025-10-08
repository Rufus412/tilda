from DictHash import DictHash
import csv

from hashtable import Hashtable



h = Hashtable(10000)






d = DictHash()
with open("Labb7/kdramaMini.txt") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        d.store(row[0], row[1:])
        h.store(row[0], row[1:])
        h.store(row[0] + "-", row[1:])
    



d.store("a", 1)
print(d.search("a"))
d.store("b", 2)
print(d.search("b"))
print(d.search("The Heirs"))
print(h.search("The Heirs-"))
print(h.search("zz"))
