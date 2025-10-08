class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key = "", data = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data


class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.table = [None] * size

    def store(self, key, data):
        """key är nyckeln
         data är objektet som ska lagras
         Stoppar in "data" med nyckeln "key" i tabellen."""
        

        index = self.hashfunction(key)
        if self.table[index] == None:
            self.table[index] = [HashNode(key, data)]
        elif (isinstance(self.table[index], list)):
            for node in self.table[index]:
                if node.key == key:
                    node.data = data
                    return
            self.table[index].append(HashNode(key, data))

    def search(self, key):
        """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
        index = self.hashfunction(key)
        if (type(self.table[index]) == list):
            for node in self.table[index]:
                if node.key == key:
                    return node.data
        raise KeyError

    def hashfunction(self, key):
        _hash = 0
        for char in str(key):
            _hash = (_hash * 11 + ord(char)) % self.size

        return _hash    