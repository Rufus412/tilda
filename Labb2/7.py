from linkedQFile import LinkedQ

# Läser in input och sparar korten samt ordning i lista.
kortLista = [x for x in input().split(" ")]

# Initierar en kortlek i form av kö
kortlek = LinkedQ()

# Lägger in alla element i kortleken
for kort in kortLista:
    kortlek.enqueue(kort)

# Här lägger vi sedan den nya ordningen
result = []

while not kortlek.isEmpty():
    # i while-loopen genomför vi korttricket
    kortlek.enqueue(kortlek.dequeue())
    result.append(kortlek.dequeue())

# utskrift
print(f"{''.join(f'{x} ' for x in result) }".strip())
