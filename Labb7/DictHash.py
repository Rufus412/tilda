class DictHash:
    def __init__(self):
        self.data = {}
    
    def store(self, key, value):
        self.data[key] = value
    
    def search(self, key):
        return self.data[key]