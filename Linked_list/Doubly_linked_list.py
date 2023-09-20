class DoubleLinkedList:
    size = 0
    head = None
    tail = None

    def __init__(self):
        self.name = 'doubly linked list'

    class Node:
        data = None

        def __init__(self, data, prev, next):
            self.data = data
            self.prev = prev
            self.next = next

        def __repr__(self):
            return ''.join(self.data)

    def clear(self):
        trav = self.head
        while trav != None:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next

        self.head = self.tail = trav = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size() == 0

    def addFirst(self, elem):
        if (self.isEmpty()):
            self.head = self.tail = self.Node(elem, None, None)
        else:
            self.head.prev = self.Node(elem, None, self.head)
            self.head.prev.next = self.head
            self.head = self.head.prev

        self.size += 1

    def addLast(self, elem):
        if (self.isEmpty()):
            self.head = self.tail = self.Node(elem, None, None)
        else:
            self.tail.next = self.Node(elem, None, self.head)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

        self.size += 1

    def add(self, elem):
        self.addLast(elem)

    def peekFirst(self):
        if (self.isEmpty()):
            print("List is empty")
            return
        return self.head.data

    def peekLast(self):
        if (self.isEmpty()):
            print("List is empty")
            return
        return self.tail.data

    def removeFirst(self):
        if (self.isEmpty()):
            print("List is empty")
            self.head = None
            self.tail = None
            return

        data = self.head.data
        next = self.head.next
        self.head.prev = self.head.next = self.value = None
        next.prev = None
        self.head = next
        self.size -= 1

        return data

    def removeLast(self):
        if (self.isEmpty()):
            print("List is empty")
            self.head = None
            self.tail = None
            return

        data = self.tail.data
        prev = self.tail.prev
        self.tail.prev = self.tail.next = self.value = None
        prev.next = None
        self.tail = prev
        self.size -= 1

        return data

    def remove(self, node):
        if (node.prev == None):
            return self.removeFirst()
        if (node.next == None):
            return self.removeLast()

        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data
        node = node.prev = node.next = node.data = None
        self.size -= 1

        return data

    def removeAt(self, index):
        if index < 0 or index >= self.size:
            print("Out of bonds")
            return
        trav = None
        if index < self.size/2:
            i = 0
            trav = self.head
            while i != index:
                trav = self.head.next
                i += 1
        else:
            i = self.size - 1
            trav = self.tail
            while i != index:
                trav = self.tail.prev
                i -= 1
        # todo revist I dont think this works
        return self.remove(trav)

    def removeByValue(self, value):
        trav = self.head
        if (value == None):
            while trav != None:
                if trav.data == None:
                    # todo revist I dont think this works
                    self.remove(trav)
                    self.len -= 1
                    return True
        else:
            while trav != None:
                if value == trav.data:
                    # todo revist I dont think this works
                    self.remove(trav)
                    self.len -= 1
                    return True

        return False

    def index(self, index):
        if index < 0 or index > self.size:
            return 'Out of bound'
        trav = self.head
        point = 0

        while point != index:
            if point == index:
                return trav.data
            trav = trav.next
            point += 1

        return -1

    def indexOf(self, value):
        trav = self.head
        point = 0

        if value == None:
            while trav != None:
                if trav.data == value:
                    return point
                trav = trav.next
                point += 0
        else:
            while trav != None:
                if trav == value:
                    return point
                trav = trav.next
                point += 1

        return -1

    def contains(self, value):
        return self.indexOf(value)

    def toString(self):
        trav = self.head
        nodeArr = []
        while trav != None:
            nodeArr.append(trav)
            trav = trav.next

        return ','.join(nodeArr)

    def removeAtExperiment(self, index):
        if index > self.size:
            print("Out of bounds")
            return
        if index == 0:
            return self.removeFirst()
        if index == self.size - 1:
            return self.removeLast()

        count = 0
        remove_node = None
        data = None
        while count < index:
            remove_node = self.head.next
            data = remove_node.data
            count += 1

        self.remove(remove_node)

        return data
