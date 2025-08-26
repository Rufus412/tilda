from linkedQFile import LinkedQ

test = LinkedQ()

print(test.isEmpty())
test.enqueue(5)
test.enqueue(1)
test.enqueue(3)
test.enqueue(4)
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())

print(test.isEmpty())
print(test.dequeue())
