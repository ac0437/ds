class PriorityQueue:
    heapSize = 0
    heapCapcity = 0
    heap = []
    hashMap = {}

    def __init__(self):
        self.name = 'priority queue'

    def size(self):
        return self.heapSize

    def isEmpty(self):
        return self.heapSize == 0

    def peek(self):
        return self.heap[0]

    def add(self, value):
        # todo: check if indexable i.e. string or number
        if self.isEmpty:
            self.heap.append(value)
            self.heapSize += 1
        else:
            self.heap.append(value)
            pos = self.heap.index(value)
            new_pos = self.bubbleUp(pos)
            self.heap[new_pos] = value
            self.heapSize += 1

    def remove(self, value):
        # find value index
        i = self.heap.index(value)
        # find last node
        last_value = self.heap[self.size - 1]
        # swap index of value with last node's value
        self.heap[i] = last_value
        self.size -= 1

        # if the value at index is greater then its children
        if self.heap[i] > self.heap[2 * i + 1] or self.heap[i] > self.heap[2 * i + 2]:
            self.bubbleDown(i)
        else:
            self.bubbleUp(i)

    def contains(self, value):
        return self.heap.index(value) >= 0

    def bubbleUp(self, pos):
        parentPosition = (pos - 1) / 2
        while pos > 0 and self.head[pos] - self.heap[parentPosition] < 0:
            self.head[pos] = self.heap[parentPosition]
            pos = parentPosition
            # we start to add two to skip silbings
            parentPosition = (parentPosition - 2) / 2
        return pos

    def bubbleDown(self, pos):
        value = self.heap[pos]
        index = 0
        # why do we care about heap size
        while pos < self.heapSize / 2:
            left = 2 * pos + 1
            right = 2 * pos + 2
            if right < self.heapSize and self.heap[left] < self.heap[right]:
                index = right
            else:
                index = left
            # min heap implementation
            if value <= self.heap[index]:
                break
            self.heap[pos] = self.heap[index]
            pos = index
        return pos
