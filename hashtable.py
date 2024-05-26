class HashTable:
    def __init__(self):
        self.size = 41
        self.table = [None] * self.size

    def hash(self, key, n):
        return (key % self.size) + n

    def insert(self, key, value):
        n = 0
        index = self.hash(key, n)
        while self.table[index] is not None:
            n += 1
            # print(f"Collision occurred at {index}")
            index = self.hash(key, n)
            # print(f"Checking index {index}")
        # print(f"Found index at {index}")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash(key, 0)
        n = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            n += 1
            index = self.hash(key, n)
            if n >= self.size:
                break
        return None
