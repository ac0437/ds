class Hashmap:
    map = {}

    def __init__(self):
        self.name = "hash map"

    def insert(self, key, value):
        self.map[key] = value

        return {key: value}

    def removeByKey(self, remove_key):
        for key in self.map:
            if key == remove_key:
                del self.map[remove_key]

        return remove_key
