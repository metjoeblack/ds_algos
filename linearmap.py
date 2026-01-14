
import random


class Map:
    
    class _MapEntry:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value

    def __init__(self) -> None:
        self._entry_list = list()

    def __len__(self):
        return len(self._entry_list)

    def __contains__(self, key):
        ndx = self._find_position(key)
        return ndx is not None

    def __iter__(self):
        for item in self._entry_list:
            yield item.key

    def __setitem__(self, key, value):
        ndx = self._find_position(key)
        if ndx is not None:
            self._entry_list[ndx].value = value
            return False
        else:
            entry = self._MapEntry(key, value)
            self._entry_list.append(entry)

    def __getitem__(self, key):
        ndx = self._find_position(key)
        if ndx is not None:
            return self._entry_list[ndx].value
        else:
            raise KeyError(f"key {key} not found")

    def remove(self, key):
        ndx = self._find_position(key)
        if ndx is not None:
            self._entry_list.pop(ndx)
        else:
            raise KeyError(f"key {key} not found")

    def _find_position(self, key):
        for i in range(len(self)):
            if self._entry_list[i].key == key:
                return i
        return None

    def key_array(self):
        unordered_keys = [key for key in self]
        random.shuffle(unordered_keys)
        return unordered_keys


def test_map():
    m = Map()
    dataset = [
        ("two", 2), ("one", 1), 
        ("three", 3), ("four", 4), ("five", 5)
    ]
    for item in dataset:
        m[item[0]] = item[1]
    print(m["one"])
    print("two" in m)
    print(len(m))
    m.remove("two")
    for i in m:
        print(i, end=" ")
    print()
    print(m.key_array())


if __name__ == "__main__":
    test_map()
    pass