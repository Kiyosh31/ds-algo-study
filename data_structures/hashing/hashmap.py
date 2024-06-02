"""
Hasmap implementation
"""


class Pair:
    """pair"""

    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap:
    """hashmap"""

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):
        """hash the key"""
        index = 0
        for c in key:
            index += ord(c)  # converts the char in ASCII code
        return index % self.capacity

    def get(self, key):
        """get the value of a key/value"""
        index = self.hash(key)

        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def put(self, key, val):
        """inserts a new key/value in hashmap"""
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return

            index += 1
            index = index % self.capacity

    def remove(self, key):
        """removes an element from hashmap"""
        if not self.get(key):
            return

        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may
                # stop searching early when it reaches this hole.
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        """rehash the hashmap"""
        self.capacity = 2 * self.capacity
        new_map = []
        for _ in range(self.capacity):
            new_map.append(None)

        old_map = self.map
        self.map = new_map
        self.size = 0
        for pair in old_map:
            if pair:
                self.put(pair.key, pair.val)

    def print(self):
        """prints the hashmap"""
        for pair in self.map:
            if pair:
                print(f"{pair.key} -> {pair.val}")


my_map = HashMap()
my_map.put("Rodrigo", "Vallarta")
my_map.put("Alice", "NYC")
my_map.print()
