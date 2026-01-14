

from collections import deque

class TreeNode:

    def __init__(self, data=None) -> None:
        self.data = data
        self.left_child = self.right_child = None

    def has_value(self, value):
        if self.data is not None:
            return self.data == value
        return False
    
    def is_leafnode(self):
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(data={self.data!r})"
    
    def __str__(self) -> str:
        return str(self.data)


def in_order(root_node):
    current = root_node
    if current is None:
        return
    else:
        in_order(current.left_child)
        print(current.data)
        in_order(current.right_child)


def pre_order(root_node):
    current = root_node
    if current is None:
        return
    print(root_node.data)
    pre_order(current.left_child)
    pre_order(current.right_child)


def post_order(root_node):
    current = root_node
    if current is None:
        return
    else:
        post_order(current.left_child)
        post_order(current.right_child)
        print(current.data)


def level_order(root_node):
    # list_of_nodes = []
    traversal_queue = deque([root_node])
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        # list_of_nodes.append(node.data)
        print(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
        if node.right_child:
            traversal_queue.append(node.right_child)
    # return list_of_nodes


def traverse_node():
    n1 = TreeNode("root node")
    n2 = TreeNode("left child node")
    n3 = TreeNode("right child node")
    n4 = TreeNode("left granchild node")
    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4
    # current = n1
    # while current:
    #     print(current.data)
    #     current = current.left_child
    in_order(n1)
    print("-" * 20)
    pre_order(n1)
    print("-" * 20)
    level_order(n1)


class TimesNode:
    """(5 + 4) * 6 + 3"""
    def __init__(self, left_child, right_child) -> None:
        self.left_child = left_child
        self.right_child = right_child
    
    def eval(self):
        return self.left_child.eval() * self.right_child.eval()
    
    
class PlusNode:

    def __init__(self, left_child, right_child) -> None:
        self.left_child = left_child
        self.right_child = right_child
    
    def eval(self):
        return self.left_child.eval() + self.right_child.eval()


class NumberNode:

    def __init__(self, num) -> None:
        self.num = num
    
    def eval(self):
        return self.num


def abstract_syntax_tree():
    x = NumberNode(5)
    y = NumberNode(4)
    p = PlusNode(x, y)
    t = TimesNode(p, NumberNode(6))
    root = PlusNode(t, NumberNode(3))
    print(root.eval())



class ExpressionTree:

    class _ExpressionTreeNode:
        operators = ("+", "-", "*", "/")

        def __init__(self, data) -> None:
            self.element = data
            self.left = None
            self.right = None
        
        def __str__(self) -> str:
            return f"{self.element}"

    def __init__(self, expr_str) -> None:
        self._expr_tree = None
        self._build_tree(expr_str)
    
    def evaluate(self, var_map):
        return self._eval_tree(self._expr_tree, var_map)
    
    def __str__(self) -> str:
        return self._build_string(self._expr_tree)
    
    def _build_tree(self, expr_str):
        pass

    def _eval_tree(self, _expr_tree, var_map):
        pass

    def _build_string(self, tree_node):
        if tree_node.left is None and tree_node.right is None:
            return str(tree_node.element)
        else:
            expr_str = "("
            expr_str += self._build_string(tree_node.left)
            expr_str += str(tree_node.element)
            expr_str += self._build_string(tree_node.right)
            expr_str += ")"
            return expr_str


class AVLNode:
    LEFT_HIGH = 1
    EQUAL_HIGH = 0
    RIGHT_HIGH = -1

    def __init__(self, data) -> None:
        self.data = data
        self.bal_factor = self.EQUAL_HIGH
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

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.h = 1 + max(self.get_height(root.left), self.get_height(root.right))
        b = self.get_balance(root)
        if b > 1 and key < root.left.data:
            return self.right_rotate(root)
        if b < -1 and key > root.right.data:
            return self.left_rotate(root)
        if b > 1 and key > root.left.data:
            return self.right_rotate(root)
        if b < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    
    def left_rotate(self, z):
        pass

    def right_rotate(self, z):
        pass

    def get_height(self, root):
        pass

    def get_balance(self, root):
        pass

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        print(root.data)
        if root.right:
            self.inorder(root.right)


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




if __name__ == "__main__":
    # traverse_node()
    # abstract_syntax_tree()
    pass

