class UnionFind:
    size = 0
    sizes = []
    ids = []
    numberOfComponents = 0

    def __init__(self):
        self.name = 'Union find'

    def create(self, size):

        if size <= 0:
            return "Size is less than or equal to 0, which is not allowed."

        self.size = self.numberOfComponents = size

        i = 0
        while i < self.size:
            self.ids.append(i)
            self.sizes.append(i)

    def find(self, p):
        root = p
        while root != self.ids[root]:
            root = self.ids[root]

        # path compression
        while p != root:
            next = self.ids[p]
            self.ids[p] = root
            p = next

        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def componentSize(self, p):
        return self.sz[self.find(p)]

    def size(self):
        return self.size

    def components(self):
        return self.numberOfComponents

    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        if (root1 == root2):
            return

        # merging
        if (self.sz[root1] < self.sz[root2]):
            self.sz[root2] += self.sz[root1]
            self.ids[root1] = self.ids[root2]
        else:
            self.sz[root1] += self.sz[root2]
            self.ids[root2] = root1

        self.numberOfComponents -= 1
