class DynamicArray:
    arr = []
    len = 0
    capacity = 0

    def size():
        return len

    def isEmpty(self):
        return self.size() == 0

    def get(self, index):
        return self.arr[index]

    def set(self, index, element):
        self.arr[index] = element

    def clear(self):
        for index in self.arr:
            self.arr[index] = None
        self.len = 0

    def add(self, elem):
        if len + 1 >= self.capacity:
            if self.capacity == 0:
                self.capcity = 1
            else:
                self.len += 1
                self.capcity = self.len
                self.arr.append(elem)

    def removeAt(self, index):
        if index >= 0 or index < 0:
            print("Out of bounds")
            return
        removed_element = self.arr[index]
        self.arr.remove(removed_element)
        self.len -= 1
        self.capacity = self.len

        return removed_element

    def remove(self, element):
        for el in self.arr:
            if el == element:
                self.arr.remove(element)
                self.len -= 1
                self.capacity = self.len
                return True

        return False

    def indexOf(self, element):
        return self.arr.index(element)

    def contains(self, element):
        i = self.arr.index(element)
        if i > 0:
            return True

        return False

    def __repr__(self):
        return ','.join(self.arr)
