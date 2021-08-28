class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for element in key:
            h += ord(element)
        return h % self.MAX

    def set_item(self, key, value):
        h = self.get_hash(key)
        is_found = False
        for index, item_tuple in enumerate(self.arr[h]):
            if key == item_tuple[0]:
                self.arr[h][index] = value
                is_found = True

        if not is_found:
            self.arr[h].append((key, value))

    def get_item(self, key):
        h = self.get_hash(key)
        is_found = False
        for item_tuple in self.arr[h]:
            if key == item_tuple[0]:
                return item_tuple[1]
        if not is_found:
            self.arr[h][1]

    def get_avrg(self, day_amount):
        temp_total = 0
        for i in range(1, day_amount + 1):
            string = f'Jan {i}'
            value = self.get_item(string)
            temp_total += value

        return round(temp_total / day_amount, 2)

    def get_max_temp(self, day_amount):
        date_temp_list = []
        temp_list = []
        for i in range(1, day_amount + 1):
            string = f'Jan {i}'
            value = self.get_item(string)
            date_temp_list.append((string, value))
            temp_list.append(value)
        max_temp_index = temp_list.index(max(temp_list))
        return date_temp_list[max_temp_index]
