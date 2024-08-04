"""
This code includes functions to find the maximum value, minimum value, 
and the sum of all values in the binary search tree (BST).
"""

class Node:
    """
    A class representing a node in a binary search tree.
    """

    def __init__(self, key):
        """
        Initialize the node with a key value.
        """
        self.left = None
        self.right = None
        self.val = key

def find_max_value(root):
    """
    Find the maximum value in a binary search tree.
    """
    current = root
    while current.right:
        current = current.right
    return current.val

def find_min_value(root):
    """
    Find the minimum value in a binary search tree.
    """
    current = root
    while current.left:
        current = current.left
    return current.val

def sum_tree_values(root):
    """
    Calculate the sum of all values in a binary search tree.
    """
    if root is None:
        return 0
    return root.val + sum_tree_values(root.left) + sum_tree_values(root.right)

def main():
    """
    Main function
    """
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    print("Найбільше значення у дереві:", find_max_value(root))
    print("Найменше значення у дереві:", find_min_value(root))
    print("Сума всіх значень у дереві:", sum_tree_values(root))

if __name__ == "__main__":
    main()
