class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for element in key:
            h += ord(element)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # probe for existing key and value
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

t = HashTable()

t['march 6'] = 130
t['march 3'] = 20
t['march 20'] = 300
t['march 11'] = 111
print(t.arr)
del t['march 6']
print(t.arr)


