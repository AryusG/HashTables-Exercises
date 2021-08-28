import csv

class HashTableLinearProbe():
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        """Hash Function"""
        h = 0
        for element in key:
            h += ord(element)
        return h % self.MAX

    def get_prob_range(self, index):
        """Returns [] of indices after inputted index. Wraps around from inputted index to the end of list
        + probing through index 0 back to one index before the inputted index"""
        return [*range(index, self.MAX)] + [*range(0, index)]

    def find_slot_index(self, key, index):
        """Returns the available hash key and allows user to change value of the same key"""
        prob_range_list = self.get_prob_range(index)
        for prob_index in prob_range_list:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hash Map is Full")

    def __setitem__(self, key, value):
        """Sets key value pairs, sends it through a hash function, places it in a hash table."""
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_slot_index(key, h)
            self.arr[new_h] = (key, value)

    def __getitem__(self, key):
        """Retrieves hashed (key, value)"""
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        print(prob_range)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if prob_index is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if prob_index is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None

t = HashTableLinearProbe()

token_list = []
with open('Resources/nyc_weather.csv', 'r') as file:
    contents = csv.reader(file)
    next(contents)
    for element in contents:
        date = element[0]
        value = int(element[1])
        token_list.append((date, value))

for token in token_list:
    t[token[0]] = token[1]


del t['Jan 9']
print(t.arr)
print(t.get_hash('Jan 10'))
print(t['Jan 10'])

# List is created
# Index 0 becomes None
# Hash for Jan 10 is 0 but because Jan 9 is also 0, it automatically routes to index 0 which is a None
# Function needs to remember where the hashed value is to get if it was moved to another slot