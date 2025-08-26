from array import array
class ArrayQ():
    def __init__(self):
        self.__elements = array("i")
    def enqueue(self, x):
        self.__elements.append(x)
    def dequeue(self):
        if not self.isEmpty():
            firstValue = self.__elements[0]
            self.__elements.remove(firstValue)
            return firstValue
        raise ValueError("array is empty")
    def size(self):
        return len(self.__elements)
    def isEmpty(self):
        return len(self.__elements) == 0
    