



def my_hash_v1(string):
    multiplier = 1
    hash_value = 0
    for cha in string:
        hash_value += multiplier * ord(cha)
        multiplier += 1
    return hash_value


test_datas = [
    "hello world", "world hello", "gello xorld",
    "ga", "ad",
]


class HashItem:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable:

    def __init__(self) -> None:
        self.size = 256
        self.slots = [None for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        multiplier = 1
        hash_value = 0
        for cha in key:
            hash_value += multiplier * ord(cha)
            multiplier += 1
        return hash_value % self.size
    
    def put(self, key, value):
        item = HashItem(key=key, value=value)
        hash_value = self._hash(key)

        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key == key:
                break
            hash_value = (hash_value + 1) % self.size
        
        if self.slots[hash_value] is None:
            self.count += 1
        self.slots[hash_value] = item
    
    def get(self, key):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key == key:
                return self.slots[hash_value].value
            hash_value = (hash_value + 1) % self.size
        
        raise KeyError(f"{key} not found")
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)


def test_hash_table():
    ht = HashTable()
    key_values =[
        ("good", "egges"), ("better", "gut"), ("best", "hostile"),
        ("ad", "do not"), ("ga", "collide")
    ]
    for item in key_values:
        ht[item[0]] = item[1]
    
    for key in [item[0] for item in key_values]:
        print(ht[key])
    
    ht.put("deserter", "shame")
    print(ht.get("deserter"))

    print(f"The hashtable has {ht.count} entries.")


test_hash_table()
