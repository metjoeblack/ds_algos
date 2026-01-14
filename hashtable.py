

class HashItem:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable:

    def __init__(self) -> None:
        self.size = 256
        self.slots = [None for _ in range(self.size)]
        self.count = 0
        self.MAX_LOADER_FACTOR = 0.65
        self.prime_number = 7
    
    def _hash(self, key):
        mult = 1
        hv = 0
        for character in key:
            hv += mult * ord(character)
            mult += 1
        return hv % self.size

    def _hash2(self, key):
        mult = 1
        hv = 0
        for character in key:
            hv += mult * ord(character)
            mult += 1
        return hv

    def __setitem__(self, key, value):
        self.put(key=key, value=value)

    def put(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        while self.slots[hash_value] != None:
            if self.slots[hash_value].key == key:
                break
            hash_value = (hash_value + 1) % self.size
        if self.slots[hash_value] == None:
            self.count += 1
        self.slots[hash_value] = item
        self._check_growth()
    
    def put_double_hashing(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        j = 1
        while self.slots[hash_value] != None:
            if self.slots[hash_value].key == key:
                break
            else:
                hash_value = (
                    hash_value + (j * (self.prime_number - (self._hash2(key) % self.prime_number)))
                ) % self.size
                j += 1
        if self.slots[hash_value] == None:
            self.count += 1
        self.slots[hash_value] = item
        self._check_growth()

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        hash_value = self._hash(key=key)
        while self.slots[hash_value] != None:
            if self.slots[hash_value].key == key:
                return self.slots[hash_value].value
            else:
                hash_value = (hash_value + 1) % self.size
        else:
            raise KeyError(f"key {key!r} not found")

    def get_double_hashing(self, key):
        hash_value = self._hash(key=key)
        j = 1
        while self.slots[hash_value] != None:
            if self.slots[hash_value].key == key:
                return self.slots[hash_value].value
            else:
                hash_value = (
                    hash_value + j * (self.prime_number - (self._hash2(key) % self.prime_number))
                ) % self.size
                j += 1
        else:
            raise KeyError(f"key {key!r} not found")

    def get_quadratic(self, key):
        hash_value = self._hash(key)
        j = 1
        while self.slots[hash_value] != None:
            if self.slots[hash_value].key == key:
                return self.slots[hash_value].value
            else:
                hash_value = (hash_value + j ** 2) % self.size
                j += 1
        return None

    def put_quadratic(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        j = 1
        while self.slots[hash_value] != None:
            if self.slots[hash_value].key == key:
                break
            hash_value = (hash_value + j ** 2) % self.size
            j += 1
        if self.slots[hash_value] == None:
            self.count += 1
        self.slots[hash_value] = item
        self._check_growth()

    def _check_growth(self):
        loader_factor = self.count / self.size
        if loader_factor > self.MAX_LOADER_FACTOR:
            print(f"Load factor before growing the hash table: {self.count / self.size}")
            self.__growth()
            print(f"Load factor after growing the hash table: {self.count / self.size}")
    
    def __growth(self):
        new_hash_table = HashTable()
        new_hash_table.size = 2 * self.size
        new_hash_table.slots = [None for _ in range(new_hash_table.size)]

        for i in range(self.size):
            if self.slots[i] != None:
                new_hash_table.put(self.slots[i].key, self.slots[i].value)
        
        self.size = new_hash_table.size
        self.slots = new_hash_table.slots



def test_hash_table():
    ht = HashTable()
    ht.put_double_hashing("good", "eggs")
    ht.put_double_hashing("better", "spam")
    ht.put_double_hashing("best", "cool")
    ht.put_double_hashing("ad", "donot")
    ht.put_double_hashing("ga", "collide")
    ht.put_double_hashing("awd", "hello")
    ht.put_double_hashing("addition", "ok")

    for key in ("good", "better", "best", "ad", "ga"):
        v = ht.get_double_hashing(key)
        print(v)
    print("The number of elements is: {}".format(ht.count))



if __name__ == "__main__":
    test_hash_table()
    pass









