class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None
    
    def enqueue(self, value):
        if self.__first:
            self.__last.next = Node(value)
            self.__last = self.__last.next
        else:
            self.__first = Node(value)
            self.__last = self.__first
        
    def dequeue(self):
        temp = self.__first
        self.__first = self.__first.next
        return temp.value
    def isEmpty(self):
        return self.__first == None