class HashTable:
    # Initialize the hash table with a size of 41
    def __init__(self):
        self.size = 41
        self.table = [None] * self.size

    # Hash function to calculate the index of the key in the table, using linear probing
    def hash(self, key, n):
        return (key % self.size) + n

    def insert(self, key, value):
        # Counter to keep track of the number of collisions
        n = 0
        index = self.hash(key, n)
        # handle collisions fusing linear probing
        while self.table[index] is not None:
            n += 1
            index = self.hash(key, n)
        self.table[index] = (key, value)

    def search(self, key):
        # initial index
        index = self.hash(key, 0)
        n = 0

        # Searching for  key in the table with linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            n += 1
            index = self.hash(key, n)
            # Stop the search upon checking all slots
            if n >= self.size:
                break
        return None
