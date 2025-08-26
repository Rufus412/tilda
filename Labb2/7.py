from linkedQFile import LinkedQ

kortLista = [x for x in input().split(" ")]

kortlek = LinkedQ()

for kort in kortLista:
    kortlek.enqueue(kort)

result = []

while not kortlek.isEmpty():
    kortlek.enqueue(kortlek.dequeue())
    result.append(kortlek.dequeue())



print(f"{''.join(f'{x} ' for x in result) }".strip())