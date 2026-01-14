

import bisect
from dataclasses import dataclass, field


def extract_names(input_file_path, output_file_path):
    with open(file=input_file_path, mode="r", encoding="utf-8") as fp_r:
        with open(file=output_file_path, mode="w", encoding="utf-8") as fp_w:
            next(fp_r)
            for line in fp_r:
                record = line.split("\t")
                fp_w.write(record[1] + "\n")


def load_names(path) -> dict:
    with open(file=path, mode="r", encoding="utf-8") as fp:
        return {name.strip(): index for index, name in enumerate(fp, start=1)}


def find_index(dataset, value):
    index = bisect.bisect_left(dataset, value)
    if index < len(dataset) and dataset[index] == value:
        return True
    return False


class SearchBy:

    def __init__(self, key_func, dataset) -> None:
        self.elements_by_key = sorted([(key_func(x), x) for x in dataset])
        self.keys = [x[0] for x in self.elements_by_key]
    
    def find(self, value):
        index = bisect.bisect_left(self.keys, value)
        if index < len(self.keys) and self.keys[index] == value:
            return self.elements_by_key[index][1]
    


@dataclass(order=True)
class Person:
    name: str
    number: int = field(compare=False)

    def __repr__(self) -> str:
        return f"{self.name.capitalize()}({self.number})"


def find_index_by_value(dataset, value):
    left_boundary, right_boundary = 0, len(dataset) - 1

    while left_boundary <= right_boundary:
        middle = (left_boundary + right_boundary) // 2

        if dataset[middle] == value:
            return middle
        
        if dataset[middle] < value:
            left_boundary = middle + 1
        elif dataset[middle] > value:
            right_boundary = middle - 1
    return None


def find_index_by_key(dataset, value, key_func):
    left_boundary, right_boundary = 0, len(dataset) - 1

    while left_boundary <= right_boundary:
        middle = (left_boundary + right_boundary) // 2
        middle_element = key_func(dataset[middle])

        if middle_element == value:
            return middle
        
        if middle_element < value:
            left_boundary = middle + 1
        elif middle_element > value:
            right_boundary = middle - 1
    return None


def find_index_mutiple(dataset, value, key_func=None):
    """Dataset must be sorted before"""
    if key_func:
        return find_index_by_value(dataset, value)
    else:
        return find_index_by_key(dataset, value, key_func)


def binary_serach_recursive(dataset, value):
    dataset = sorted(dataset)

    def recursive(left_boundry, right_boundry):
        if left_boundry <= right_boundry:
            # middle = (left_boundry + right_boundry) // 2
            middle = left_boundry + (right_boundry - left_boundry) // 2
            if dataset[middle] == value:
                return True
            if dataset[middle] < value:
                return recursive(middle + 1, right_boundry)
            elif dataset[middle] > value:
                return recursive(left_boundry, middle - 1)
        return False
    return recursive(0, len(dataset) - 1)


def bisect_usage():
    sorted_fruits = [
        "apple", 
        "banana", 
        "banana", 
        "banana", 
        "orange", 
        "strawberry", 
        "plum"
    ]
    print(bisect.bisect_left(sorted_fruits, "banana"))
    print(bisect.bisect_right(sorted_fruits, "banana"))
    print(bisect.bisect_left(sorted_fruits, "plum"))
    print(bisect.bisect_left(sorted_fruits, "watermelon"))
    print(find_index(sorted_fruits, "orange"))
    print(find_index(sorted_fruits, "watermelon"))
    left_index = bisect.bisect_left(sorted_fruits, "banana")
    right_index = bisect.bisect_right(sorted_fruits, "banana")
    banana_quantity = right_index - left_index
    print(banana_quantity)

    # insert value
    bisect.insort(sorted_fruits, "apricot")
    print(sorted_fruits)
    bisect.insort_left(sorted_fruits, "orange")
    print(sorted_fruits)


if __name__ == "__main__":
    source_path = r"/home/shangguan/Downloads/name.basics.tsv/data.tsv"
    output_path = r"/home/shangguan/Downloads/name.basics.tsv/names.txt"
    # extract_names(source_path, output_path)
    # name_dict = load_names(output_path)
    # print("Arnold Schwarzenegger" in name_dict)
    # print(name_dict["Arnold Schwarzenegger"])
    p1 = Person("John", 1)
    p2 = Person("John", 2)
    print(p1 == p2)
    print(p1 is p2)
    print(p1)
    print(p2)
    alice = Person('Alice', 1)
    bob = Person("Bob", 1)
    print(alice < bob)
