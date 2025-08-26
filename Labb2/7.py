from linkedQFile import LinkedQ

kortLista = [int(x) for x in input("Vilken ordning ligger korten i?").split(" ")]

kortlek = LinkedQ()

for kort in kortLista:
    kortlek.enqueue(kort)

result = []

while not kortlek.isEmpty():
    kortlek.enqueue(kortlek.dequeue())
    result.append(kortlek.dequeue())



print(f"de kommer ut i denna ordning {''.join(f'{x} ' for x in result) }"  )