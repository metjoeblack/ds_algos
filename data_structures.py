from collections import deque, Counter
from io import StringIO
import re
from collections.abc import Iterable, Sequence
import functools

from custom_exceptions import ValueNotFoundError

class ListNode:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None    #  defualt as None, as the tail node
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(data={self.data})"
    
    def __str__(self) -> str:
        return f"{self.data}"
    
    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


class LinkedList:
    def __init__(self, initial_value=None) -> None:
        """
        Create a new singly-linked list. 
        Take O(1) time.
        """
        self.head = None
        if initial_value is not None:
            try:
                for item in initial_value:
                    self.append(item)
            except TypeError:
                new_node = ListNode(data=initial_value)
                self.head = new_node

    
    def __repr__(self):
        """
        Show the content in the list.
        """
        contents = list()
        current_node = self.head
        while current_node:
            contents.append(current_node.data)
            current_node = current_node.next
        
        return " -> ".join([str(item) for item in contents])
    
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            # yield the node , not the data of node.
            current_node = current_node.next
    
    def __getitem__(self, index):
        """
        Get the data of the node according the specified index in the list.
        """
        if self.index_verification(index=index):
            current_idx = 0
            current_node = self.head
            for current_node in self:
                if current_idx == index:
                    return current_node.data
                current_idx += 1

    def __contains__(self, data) -> bool:
        """
        Search for the first element with `data` matching `data`. 
        Return False if not found.
        Takes O(n) time.
        """
        if not self.is_empty():
            for current_node in self:
                if current_node.has_value(data):
                    return True
        return False

    def __len__(self):
        """
        Get the length of the list.
        Take O(n) time.
        """
        counter = 0
        for _ in self:
            counter += 1
        return counter

    def __reversed__(self):
        pass

    def append(self, data):
        """
        Insert a new element at the end of the list. 
        Take O(1) time.
        """
        if not isinstance(data, LinkedList):
            new_node = ListNode(data=data)
        else:
            new_node = data

        if self.head is None:
            self.head = new_node
            return
        else:
            # current_node = self.head
            # while current_node.next is not None:
            #     current_node = current_node.next
            for current_node in self:
            # traverse the linked list to the end
                pass
            current_node.next = new_node
    
    def display(self):
        """
        Show the content in the list.
        """
        contents = list()
        current_node = self.head
        while current_node:
            contents.append(current_node.data)
            current_node = current_node.next
        print(contents)
    
    def remove_index(self, index):
        """
        Remove the the node at specified index in the list.
        Take O(n) time.
        """
        if self.index_verification(index=index):
            if index == 0:
                self.popleft()
                return
            current_node = self.head
            current_idx = 0
            for current_node in self:
                previous_node = current_node
                current_node = current_node.next
                current_idx += 1
                if current_idx == index:
                    previous_node.next = current_node.next
                    break
    
    def remove_data(self, data):
        """
        Remove the first occurrence of 'data' in the list.
        Take O(n) time.
        """
        # Find the element and keep a reference to the element preceding it.
        if data in self:
            current_node = self.head
            if self.head.has_value(data):
                self.head = current_node.next
                return
            for current_node in self:
            # also: while current_node:
                previous_node = current_node
                current_node = current_node.next
                if current_node.has_value(data):
                    previous_node.next = current_node.next
                    break
        else:
            raise LookupError(f"Error: {data} not exsits.")

    def insert(self, index, data) -> None:
        """
        Insert a new ListNode with the given data at the given index in the list.
        Take O(1) time.
        """
        if isinstance(index, int):
            if index > self.__len__() or index < 0:
                raise IndexError(f"Error: Index {index} out of range!")
        else:
            raise TypeError(f"Expected an integer (>=0), but given a {type(index)}.")
        
        if not isinstance(data, LinkedList):   
            new_node = ListNode(data=data)
        else:
            new_node = data

        if index == self.__len__():
            self.append(data=data)
            return
        current_node = self.head
        current_idx = 0
        if index == 0:
            self.head = new_node
            new_node.next = current_node
            return
        while current_node:
            previous_node = current_node
            current_node = current_node.next
            current_idx += 1
            if current_idx == index:
                previous_node.next = new_node
                new_node.next = current_node
    
    def count(self, data):
        """
        Count the number of occurrences of the given data in the list.
        Take O(n) time.
        """
        current_node = self.head
        counter = 0
        while current_node:
            if current_node.has_value(data):
                counter += 1
            current_node = current_node.next
        
        return counter

    def replace_all(self, old_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == old_data:
                current_node.data = new_data
            current_node = current_node.next

    def pop(self):
        if not self.is_empty():
            current_node = self.head
            
            if current_node.next is None:
                self.head = None
                return current_node.data
            
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            return current_node.data
        else:
            raise IndexError("pop from empty linked_list.")

    def popleft(self):
        if not self.is_empty():
            current_node = self.head
            
            if current_node.next is None:
                self.head = None
                return current_node.data

            previous_node = current_node
            current_node = current_node.next
            self.head = current_node
            return previous_node.data
        else:
            raise IndexError("pop from empty linked_list.")

    def reverse(self):
        """
        Reverse the list in-place. 
        Take O(n) time.
        """
        if not self.is_empty():
            if self.__len__() == 1:
                return None
            else:
                previous_node = None
                current_node = self.head
                while current_node is not None:
                    next_node = current_node.next
                    current_node.next = previous_node     # change the reference.
                    previous_node = current_node
                    current_node = next_node
                self.head = previous_node

        else:
            raise IndexError(r"Error: Empty linked_list, can't to be reversed.")

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def index_verification(self, index) -> bool:
        """
        Verify the legitimacy of the given index value.
        Return True if the index is not out of the length.
        """
        try:
            if isinstance(index, int):
                if self.head is None:
                    raise IndexError("Error: empty linked_list")
                total_length = self.__len__()
                if index >= total_length or index < 0:
                    raise IndexError(f"Error: Index {index} out of range(0 <= index < {total_length})!")
            else:
                raise TypeError(f"Expected an integer (>=0), but given a {type(index)} type.")
        except (IndexError, TypeError):
            return False
        else:
            return True


def linked_list():
    lst = LinkedList([12, "23", "a", 2, "X", "God", "let", "K", 2])

    print(lst)
    print(repr(lst))

    for item in lst:
        print(item)
    
    print(lst[2])

    print("X" in lst)

    print(len(lst))

    lst.append("Assimilate")

    lst.display()

    lst.remove_index(0)

    lst.remove_data("a")

    lst.insert(0, "Start")

    lst.insert(3, "K")

    print("K: ", lst.count("K"))

    lst.replace_all(2, 2000)

    lst.display()

    print(lst.pop())

    print(lst.popleft())

    lst.reverse()

    lst.display()

linked_list()


class DoubleLinkedListNode:
    
    def __init__(self, pre=None, data=None, next=None) -> None:
        self.pre = pre
        self.data = data
        self.next = next
    
    def has_value(self, data):
        if self.data == data:
            return True
        return False


class DoubleLinkedList:
    
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        if not isinstance(data, DoubleLinkedListNode):
            new_node = DoubleLinkedListNode(data=data)
        else:
            new_node = data
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.pre = current_node
        # current_node.next = DoubleLinkedListNode(data=data, pre=current_node)
    
    def length(self):
        total_length = 0
        if not self.is_empty():
            current_node = self.head
            while current_node:
                total_length += 1
                current_node = current_node.next
        return total_length

    
    def display(self) -> list:
        contents = list()
        current_node = self.head

        while current_node:
            contents.append(current_node.data)
            current_node = current_node.next
        print(contents)
    

    def find(self, data):
        if not self.is_empty():
            current_node = self.head
            while current_node:
                if current_node.has_value(data=data):
                    return current_node.data
                current_node = current_node.next
        return None
    
    def insert(self, index, data):
        if self.is_empty():
            self.head = DoubleLinkedListNode(pre=None, data=data, next=None)
        
        if index == self.__len__():
            self.append(data=data)
            return
        
        current_node = self.head
        current_idx = 0
        while current_node:
            previous_node = current_node
            current_node = current_node.next
            current_idx += 1
            if current_idx == index:
                new_node = DoubleLinkedListNode(pre=previous_node, data=data, next=current_node)
                previous_node.next = new_node
                current_node.pre = new_node


    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        

def doubule_linked_list():
    dlst = DoubleLinkedList()

    dlst.insert(0, 100)

    dlst.display()

    dlst.append(2)
    dlst.append("Q")

    data = ["23", 12, "X", "God"]
    for item in data:
        dlst.append(item)
    
    dlst.display()

    dlst.insert(7, 7)

    dlst.display()

    dlst.insert(3, "End")

    dlst.display()


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data):
        pass

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        current_node = starting_point
        while current_node is not None and (current_node.next != starting_point):
            yield current_node
            current_node = current_node.next
        yield current_node
        

def top_k_frequency_v2(num_array: list):
    counter = Counter(num_array)
    return counter.most_common(2)


# print(top_k_frequency_v2([2,0,0,2,1,10,2,10,12,2]))


def words_counter(file_path: str):
    words_counter = Counter()
    separator = r" |,|!|\.|-|\*|\n"
    with open(file_path, "r", encoding="utf-8", newline=None) as file_pointer:
        for line in file_pointer:
            # r" |,|!|\.|-|\*|\n"
            line_words =  [item for item in re.split(separator, line) if item]
            # line_words = line.strip(",.-*!").split()
            words_counter.update(Counter(line_words))
    
    for item in words_counter.most_common():
        print(item)

    return words_counter.most_common(1)


# print(words_counter("/home/shangguan/Downloads/Pyzen.txt"))


def mode(data):
    counter = Counter(data)
    _, top_count = counter.most_common(1)[0]
    return [point for point, count in counter.items() if count == top_count]

# print(mode([2,0,0,1,10,8,10,2,12,3,5,10,7,2]))


class CustomQueue:

    def __init__(self) -> None:
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None
    
    def __len__(self):
        return len(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __iter__(self):
        yield from self._items
    
    def __reversed__(self):
        yield from reversed(self._items)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"


@functools.total_ordering
class BinarySearchTreeNode:

    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__!r}(value={self.value!r})"
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return False
    
    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return False
    
    def has_value(self, value) -> bool:
        if value == self.value:
            return True
        else:
            return False


class BinarySearchTree:

    def __init__(self, initials=None) -> None:
        self.root = None
        
        if initials is not None:
            try:
                for item in initials:
                    self.insert(self.root, item)
            except TypeError:
                self.insert(self.root, initials)

    def insert(self, current, value) -> None:
        """
        Insertion in Binary Search Tree using Recursion.
        """
        if self.root is None:
            self.root = BinarySearchTreeNode(value=value)
            return
        else:
            if value < current.value:
                if current.left is None:
                    current.left = BinarySearchTreeNode(value=value)
                else:
                    self.insert(current.left, value=value)
            elif value >= current.value:
                if current.right is None:
                    current.right = BinarySearchTreeNode(value=value)
                else:
                    self.insert(current.right, value=value)
    
    def insert_iteration(self, value) -> None:
        """
        Insertion in Binary Tree using Iterative approach
        """
        new_node = BinarySearchTreeNode(value=value)
        
        if self.root is None:
            self.root = new_node
            return
        
        pre_node = None
        current_node = self.root
        
        while current_node is not None:     # core code!
            if value < current_node.value:
                pre_node = current_node
                current_node = current_node.left
            elif value >= current_node.value:
                pre_node = current_node
                current_node = current_node.right
        
        if value < pre_node.value:
            pre_node.left = new_node
        else:
            pre_node.right = new_node
    
    def search(self, current_node, value) -> bool:
        """
        Search using Recursion.
        """
        if current_node is None:
            return False
        else:
            if current_node.has_value(value):
                return True
            elif value < current_node.value:
                if current_node.left is None:
                    return False
                else:
                    return self.search(current_node.left, value=value)
            elif value > current_node.value:
                if current_node.right is None:
                    return False
                else:
                    return self.search(current_node.right, value=value)
    
    def search_iteration(self, value) -> bool:
        """
        Search using Itearative approach.
        """
        if self.root is None:
            return False
        else:
            current_node = self.root
            
            while current_node is not None:
                if current_node.has_value(value=value):
                    return True
                elif value < current_node.value:
                    current_node = current_node.left
                elif value > current_node.value:
                    current_node = current_node.right
            
            return False
    
    def delete(self, value):
        """
        To delete a node from BST, there are three possible situations occurs:
            1. The node to be deleted is the leaf node, or,
            2. The node to be deleted has only one child, and,
            3. The node to be deleted has two children.
        The first tow are so easy, however the third is a bit complex among other tow cases.In such a case, the steps are as follows:
            1). First, find the inorder successor of the node to be deleted.
            2). After that, replace that node with the inorder successor until the target node is placed at the leaf of tree.
            3). And at last, replace the node with NULL and free up the allocated space.
        To make it less difficult to understand, you can start without considering the duplicate values. Once that is done,
        then you can try to consider the delete operation that deals with duplicate values.
        """
        if self.is_empty():
            raise ValueError(f"Empty tree, Deletion is cancelled")
        
        if self.is_only_root():
            if value == self.root.value:
                self.root = None
                return value
            else:
                raise ValueNotFoundError(value=value)
        
        pre_node = None
        current_node = self.root
        while current_node is not None:
            if current_node.has_value(value=value):
                if (current_node.left is None) and (current_node.right is None):
                # the node to be deleted is the leaf node.
                    if value < pre_node.value:
                        pre_node.left = None
                    if value > pre_node.value:
                        pre_node.right = None
                
                elif (current_node.left is not None) and (current_node.right is not None):
                # the node to be deleted has two child node.
                    inorder_successor_node = current_node.right
                    while (inorder_successor_node.left is not None) and inorder_successor_node.left.value != value:
                    # Must consider the duplicate value during the deletion.
                        inorder_successor_node = inorder_successor_node.left
                    
                    # if duplicate values are encountered, then break on the left side of inorder_successor_node.
                    inorder_successor_node.left = None

                    temp = inorder_successor_node.value
                    self.delete(value=inorder_successor_node.value)
                    current_node.value = temp

                else:
                # the node to be deleted has one child node.
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.left = None
                    else:
                        current_node.value = current_node.right.value
                        current_node.right = None
                
                # if found, delete it, and return the value
                return value
                
            elif value < current_node.value:
                pre_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                pre_node = current_node
                current_node = current_node.right
        
        raise ValueNotFoundError(value=value)
    
    def count(self, value) -> int:
        counter = 0
        if self.root is None:
            return counter
        else:
            current_node = self.root
            
            while current_node is not None:
                if current_node.has_value(value):
                    counter += 1
                    current_node = current_node.right
                elif value < current_node.value:
                    current_node = current_node.left
                elif value > current_node.value:
                    current_node = current_node.right
        
        return counter
    

    def is_balanced(self):
        pass


    def get_height(self):
        pass


    def is_empty(self):
        return self.root is None
    

    def is_only_root(self):
        if self.root is not None:
            if self.root.left is None and self.root.right is None:
                return True
        return False

    
    def inorder(self, current_node):
        if current_node:
            # traverse left
            self.inorder(current_node.left)
            # traverse root
            print(str(current_node.value) + '->', end="")
            # traverse right
            self.inorder(current_node.right)
    
    def preorder(self, current_node):
        if current_node:
            # traverse root
            print(str(current_node.value) + '->', end="")
            # traverse left
            self.preorder(current_node.left)
            # traverse right
            self.preorder(current_node.right)
    
    def postorder(self, current_node):
        pass


def binary_search_tree():
    bst = BinarySearchTree([45, 15, 79])
    
    def test_and_count():
        insert_test = [90, 10, 55, 12, 20, 50, 17, 23, 95, 58, 9]
        [bst.insert(bst.root ,k) for k in insert_test]

        bst.inorder(bst.root)
        print()

        search_test = [45, 15, 30, 50, 41, 77]
        print([bst.search(bst.root, item)  for item in search_test])
        print([bst.search_iteration(i)  for i in search_test])

        duplicate_insert = [45, 15, 20, 15, 20, 45]
        [bst.insert_iteration(m) for m in duplicate_insert]
    
        count_test = [20, 55, 15, 45]
        print("Count test: ", end="")
        print([bst.count(j) for j in count_test])

        delete_test = [45, 15, 79, 20, 19]
        try:
            for it in delete_test:
                print(bst.delete(it))
                bst.inorder(bst.root)
                print()
        except ValueNotFoundError as err:
            print(err)
    
    test_and_count()
    
# binary_search_tree()



class AVLTree:
    pass





