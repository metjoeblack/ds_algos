
from trees import TreeNode
from typing import Generator
from queues import LinkedListBasedQueue
import ctypes
from stacks import Stack
from bintrees.avltree import AVLTree


class Array1D:

    def __init__(self, size) -> None:
        assert size > 0
        self._size = size

        # Create the array structure using the ctypes module
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initialize each element.
        self.clear(None)
    
    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self)
        return self._elements[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self)
        self._elements[index] = value
    
    def clear(self, value=None):
        """Clears the array by setting each element to the given value."""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return self._ArrayIterator(self._elements)

    class _ArrayIterator:
        
        def __init__(self, the_array) -> None:
            self._array_ref = the_array
            self._current_index = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._current_index < len(self._array_ref):
                entry = self._array_ref[self._current_index]
                self._current_index += 1
                return entry
            else:
                raise StopIteration


class DepthFirstMixin:

    def in_order(self):
        def inner_in_order(root_node):
            current = root_node
            if current is None:
                return
            else:
                inner_in_order(current.left_child)
                print(current.data, end=" ")
                inner_in_order(current.right_child)
        inner_in_order(self.root_node)
        print()

    def pre_order(self):
        def inner_pre_order(root_node):
            current = root_node
            if current:
                print(current.data, end=" ")
                inner_pre_order(current.left_child)
                inner_pre_order(current.right_child)
        inner_pre_order(self.root_node)
        print()

    def post_order(self):
        def inner_post_order(root_node):
            current = root_node
            if current:
                inner_post_order(current.left_child)
                inner_post_order(current.right_child)
                print(current.data, end=" ")
        inner_post_order(self.root_node)
        print()


class BreadthFirstMinx:
    
    def level_order(self):
        
        def inner(root_node):
            q = LinkedListBasedQueue()
            q.enqueue(root_node)
            while not q.is_empty():
                node = q.dequeue()
                print(node.data)
                if node.left_child is not None:
                    q.enqueue(node.left_child)
                if node.right_child is not None:
                    q.enqueue(node.right_child)
        
        inner(self.root_node)


class BinarySearchTree(DepthFirstMixin):

    def __init__(self) -> None:
        self.root_node = None

    def __str__(self) -> str:
        return " ".join(str(node.data) for node in self)
    
    def __iter__(self):
        return self.in_order_gen()
    
    def __contains__(self, value):
        current = self.root_node
        while True:
            if current is None:
                return False
            if value == current.data:
                return True
            else:
                if value < current.data:
                    current = current.left_child
                elif value > current.data:
                    current = current.right_child

    def in_order_gen(self) -> Generator:
        def inner(root_node):
            current = root_node
            if current:
                if current.left_child:
                    yield from inner(current.left_child)
                yield current
                if current.right_child:
                    yield from inner(current.right_child)
        return inner(self.root_node)

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root_node is None:
            self.root_node = new_node
        else:
            current = self.root_node
            while True:
                if value < current.data:
                    if current.left_child is None:
                        current.left_child = new_node
                        break
                    current = current.left_child
                else:
                    if current.right_child is None:
                        current.right_child = new_node
                        break
                    current = current.right_child
    
    def extend(self, iterables):
        for item in iterables:
            self.insert(item)

    def delete(self, value):
        current = self.root_node
        while True:
            if current is None:
                raise ValueError(f"value {value!r} not found in the tree.")
            if current.has_value(value=value):
            # find the node
                if current.is_leafnode():
                # delete leaf node(no child)
                    if current is parent.left_child:
                        parent.left_child = None
                    else:
                        parent.right_child = None
                elif (current.left_child and current.right_child):
                # delete the node with two children, complicated!
                    successor = current.right_child
                    if successor.is_leafnode():
                    # the successor has not child
                        current.data = successor.data
                        current.right_child = None
                    elif (successor.right_child and successor.left_child):
                    # the successor has two child
                        while successor.left_child:
                        # find the leftmost node of left subtree of the successor the current node 
                            parent_of_successor = successor
                            successor = successor.left_child
                        current.data = successor.data
                        if successor.right_child is None:
                            parent_of_successor.left_child = None
                        else:
                            parent_of_successor.left_child = successor.right_child
                    else:
                    # the successor has one child(right_child)
                        if successor.right_child is not None:
                            current.data = successor.data
                            current.right_child = successor.right_child
                        else:
                            current.data = successor.left_child.data
                            successor.left_child = None
                else:
                # delete the node with one child
                    if current.left_child is not None:
                        current.data = current.left_child.data
                        current.left_child = None
                    else:
                        current.data = current.right_child.data
                        current.right_child = None
                break
            else:
                parent = current         # set the parent node
                if value < current.data:
                    current = current.left_child
                elif value > current.data:
                    current = current.right_child

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current.data

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current.data

    def is_unique(self):
        temp = -1
        for node in self:
            if node.data != temp:
                temp = node.data
            else:
                return False
        return True
    
    def print_all_leaf(self):

        def _print_leaf_helper(root):
            # If node is null , return
            if not root:
                return
            # If node is leaf node, print its data
            if not root.left_child and not root.right_child:
                print(root.data, end=", ")
                return
            # If left child exists, check for leaf recursively
            if root.left_child is not None:
                _print_leaf_helper(root.left_child)
            # If right child exists, check for leaf recursively
            if root.right_child is not None:
                _print_leaf_helper(root.right_child)
        
        _print_leaf_helper(self.root_node)
        


def test_bst():
    bst = BinarySearchTree()
    dataset = [10, 7, 3, 13, 9, 6, 16, 4, 13, 2, 9, 17, 8, 12]
    for i in dataset:
        bst.insert(i)
    print(bst)
    bst.in_order()
    bst.pre_order()
    bst.post_order()
    # bst.delete(13)
    # bst.in_order()
    # bst.delete(3)
    # bst.in_order()
    print(15 in bst)
    print(16 in bst)
    print(bst.find_max())
    print(bst.find_min())
    print(bst.is_unique())
    bst.print_all_leaf()


test_bst()


def binary_tree():
    dataset = [10, 7, 3, 13, 6, 16, 4, 13, 9, 17, 8, 12]
    # my_tree = tree(height=4, is_perfect=True)
    # print(my_bsttree)
    # tree_1 = build2(dataset)
    # print(tree_1)
    dataset = [40,20,60,10,30,50,70]
    bst = BinarySearchTree()
    bst.extend(dataset)
    bst.in_order()
    bst.insert(25)
    bst.in_order()



class BSTree:

    class __Node:
        """This is a Node class that is internal to the BSTree class."""
        def __init__(self, value, left_child=None, right_child=None) -> None:
            self.value = value
            self.left_child = left_child
            self.right_child = right_child
        
        def get_value(self):
            return self.value
        
        def set_value(self, new_value):
            self.value = new_value
        
        def get_left(self):
            return self.left_child
        
        def get_right(self):
            return self.right_child
        
        def set_left(self, new_left):
            self.left_child = new_left

        def set_right(self, new_right):
            self.right_child = new_right
        
        def __iter__(self):
            if self.left_child != None:
                for element in self.left_child:
                    yield element
            yield self.value
            if self.right_child != None:
                for element in self.right_child:
                    yield element

    # Below are the methods of the BSTree class
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, new_value):
        """
        The __insert() function is recursive and is not a passed a self parameter. 
        It is a static function (not a method of the class) but is hidden inside 
        the insert() method so users of the class will not know it exists.
        """
        def __insert(root, new_value):
            if root == None:
                return BSTree.__Node(value=new_value)
            if new_value < root.get_value():
                root.set_left(__insert(root.get_left(), new_value))
            else:
                root.set_right(__insert(root.get_right(), new_value))
            return root

        self.root = __insert(self.root, new_value)
    
    def delete(self, value):
        """Just like the insert() method ...."""
        def __delete(root, value):
            pass
        __delete(self.root, value)
    
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def use_bst():
    lst = [13, 2, 19, 7, 4, 29, 18, 5, 9, 23]
    tree = BSTree()
    for x in lst:
        tree.insert(float(x))
    for j in tree:
        print(j, end="  ")


class BSTMap:

    class _BSTMapNode:
        """
        Storage class for the binary search tree nodes of the map
        """
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value
            self.left = None
            self.right = None
        
        def has_value(self, value):
            return self.value == value
        
        def set_value(self, value):
            self.value = value
        
        def is_leaf(self):
            return self.left is None and self.right is None
        
        def __str__(self) -> str:
            return f"{self.value}"

    def __init__(self) -> None:
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return self._bst_search(self._root, key) is not None

    def value_of_key(self, key):
        node = self._bst_search(self._root, key)
        assert node is not None
        return node.value
    
    def _bst_search(self, subtree, target):
        if subtree is None:
            return None
        elif target == subtree.key:
            return subtree
        elif target < subtree.key:
            return self._bst_search(subtree.left, target)
        else:
            return self._bst_search(subtree.right, target)
    
    def insert(self, key, value):
        # Find the node containg the key, if it exists.
        node = self._bst_search(self._root, key)
        # If the key is already in the tree, update its value.
        if node is not None:
            node.value = value
            return False
        else:
        # Otherwise, add a new entry.
            self._root = self._bst_insert(self._root, key, value)
            self._size += 1
            return True

    def _bst_insert(self, subtree, key, value):
        if subtree is None:
            subtree = self._BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree
    
    def remove(self, key):
        assert key in self
        self._root = self._bst_remove(self._root, key)
        self._size -= 1

    def _bst_remove(self, subtree, target):
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bst_remove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._bst_remove(subtree.right, target)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._bst_minimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._bst_remove(subtree.right, successor.key)
                return subtree
    
    def min(self):
        return self._bst_minimum(self._root)
    
    def _bst_minimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_minimum(subtree.left)

    def __iter__(self):
        """
        Return an iterator for traversing the keys in the map
        """
        # return self._BSTMapIterator(self._root, self._size)
        return self._BSTMapStackIterator(self._root)
    
    class _BSTMapIterator:
        
        def __init__(self, root, size) -> None:
            self._the_keys = Array1D(size)
            self._cur_item = 0
            self._bst_traversal(root)
            self._cur_item = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._cur_item < len(self._the_keys):
                node = self._the_keys[self._cur_item]
                self._cur_item += 1
                return node
            else:
                raise StopIteration
        
        def _bst_traversal(self, subtree):
            """Perform an inorder traversal used to build the array of keys"""
            if subtree is not None:
                self._bst_traversal(subtree.left)
                self._the_keys[self._cur_item] = subtree
                self._cur_item += 1
                self._bst_traversal(subtree.right)
    
    class _BSTMapStackIterator:
        """Iterator Based on stack"""
        def __init__(self, root) -> None:
            self._the_stack = Stack()
            self._traversal_to_min_node(root)
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._the_stack.is_empty():
                raise StopIteration
            else:
                node = self._the_stack.pop()
                if node.right is not None:
                    self._traversal_to_min_node(node.right)
                return node
        
        def _traversal_to_min_node(self, subtree):
            if subtree is not None:
                self._the_stack.push(subtree)
                self._traversal_to_min_node(subtree.left)


def test_bst_map():
    keys = [57, 32, 12, 98, 37, 81, 72, 54, 67, 17]
    bst_map = BSTMap()
    for key in keys:
        bst_map.insert(key, key ** 2)
    print(bst_map._root)
    print(bst_map.min())
    for item in bst_map:
        print(item)



# test_bst_map()


class AVLMapNode:
    LEFT_HIGH = 1
    EQUAL_HIGH = 0
    RIGHT_HIGH = -1

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.balanced_factor = self.EQUAL_HIGH
        self.left = None
        self.right = None


class AVL:

    def __init__(self) -> None:
        self._root = None
        self._size = 0
    
    def __contains__(self, key):
        pass

    def _bst_search(self, key):
        pass

    def insert(self, key, value):
        pass

    def _avl_insert(self, key, value):
        pass

    def remove(self, key):
        pass

    def _avl_remove(self, key):
        pass

    def _avl_rotate_right(self, pivot):
        pass

    def _avl_rotate_left(self, pivot):
        pass

    def __iter__(self):
        pass

    class _AVLMapIterator:

        def __init__(self) -> None:
            pass


def use_avl():
    avl = AVLTree()
    dataset = [10, 15, 5, 1, 12, 6, 18]
    for key in dataset:
        avl.insert(key, value=key ** 2)
    for key in avl:
        print(key, avl.get_value(key))
    
# use_avl()


if __name__ == "__main__":
    # test_bst()
    # use_bst()
    pass
    # binary_tree()

