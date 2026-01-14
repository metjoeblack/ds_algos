
from collections import Counter
import string


class HashItem:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable:

    def __init__(self) -> None:
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65

    def _hash(self, key):
        mult = 1
        hv = 0
        for character in key:
            hv += mult * ord(character)
            mult += 1
        return hv % self.size
    
    def put(self, key, value):
        item = HashItem(key=key, value=value)
        h = self._hash(key=key)
        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()
    
    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor > self.MAXLOADFACTOR:
            print("Load factor before growing the hash table: ", self.count / self.size )
            self.growth()
            print("Load factor after growing the hash table: ", self.count / self.size )
        
    def growth(self):
        New_Hash_Table = HashTable()
        New_Hash_Table.size = 2 * self.size
        New_Hash_Table.slots = [None for _ in range(New_Hash_Table.size)]

        for i in range(self.size):
            if self.slots[i] != None:
                New_Hash_Table.put(self.slots[i].key, self.slots[i].value)
        
        self.size = New_Hash_Table.size
        self.slots = New_Hash_Table.slotss

    def get(self, key):
        h = self._hash(key=key)
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + 1) % self.size
        return None
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)



def distribute(items, num_containers, hash_func=hash):
    return Counter(
        [hash_func(item) % num_containers for item in items]
    )


def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")


def myhash(text):
    return sum(
        index * ord(character) 
        for index, character in enumerate(repr(text).lstrip("'"), start=1)
    )


if __name__ == "__main__":
    # plot(distribute(string.printable, num_containers=20))
    print(myhash("Lorem"))
    print(myhash("Loren"))
    print(myhash("Loner"))
    print(myhash(3.14))
    print(myhash("3.14"))
    print(myhash(True))
    plot(distribute(string.printable, num_containers=6, hash_func=myhash))






