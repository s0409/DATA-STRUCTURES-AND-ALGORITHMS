class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data





# we recursively call the mirror function which swaps the right subtree with the left subtree.
def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)


print(mirror(root))
