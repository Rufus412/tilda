from Labb2.arrayQFile import *



kortLista = [int(x) for x in input("Vilken ordning ligger korten i?").split(" ")]

kortlek = ArrayQ()

for kort in kortLista:
    kortlek.enqueue(kort)

result = []

while not kortlek.isEmpty():
    kortlek.enqueue(kortlek.dequeue())
    result.append(kortlek.dequeue())

print("de kommer ut i denna ordning " + f"{result}")