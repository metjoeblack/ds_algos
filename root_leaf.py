
class TreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def build_tree(target_str):
    pass




def is_leafnode(node):
    return node.left is None and node.right is None


def print_root_to_leaf_paths(node, path):
    if node is None:
        return
    
    path.append(node.data)

    if is_leafnode(node):
        print(list(path))
    
    print_root_to_leaf_paths(node.left, path)
    print_root_to_leaf_paths(node.right, path)

    path.pop()


def main(root):
    path = []
    print_root_to_leaf_paths(root, path)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(8)
    root.right.right.right = TreeNode(9)

    main(root)






