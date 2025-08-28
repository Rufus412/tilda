
class Node:
    # Nodklass för att representera varje element i kön
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQ:
    # Kön
    def __init__(self):
        #Initierar kön som tom
        self.__first = None
        self.__last = None
    
    def enqueue(self, value):
        #Lägger till en nod och dess värde sist i kön.
        if self.__first:
            # Om det finns åtminstone ett element så skapar vi en ny
            # nod och sätter den som sist.
            self.__last.next = Node(value)
            self.__last = self.__last.next
        else:
            # Om ingen första nod finns skapar vi en nod och sätter
            # den som först samt sist
            self.__first = Node(value)
            self.__last = self.__first
        
    def dequeue(self):
        # Tar bort första elementet och returnerar dess värde
        temp = self.__first
        self.__first = self.__first.next
        return temp.value
    def isEmpty(self):
        # Kollar och returnerar om kön är tom.
        return self.__first == None