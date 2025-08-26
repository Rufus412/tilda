from array import array

a = array("i", [1, 3, 2, 4])
print(a)

a.append(7)
print(a)
print(a[3])
print(a.pop())
print(a)
a.remove(2)
print(a)
a.insert(3, 9)
print(a)