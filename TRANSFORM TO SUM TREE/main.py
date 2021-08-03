class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def toSumTree(root):
    #base case
    if root is None:
        return 0
    #store the old value
    old=root.data

    #recursively call for left and right subtrees
    root.data = toSumTree(root.left) + \
                toSumTree(root.right)
    return root.data+old
#utility function to print inorder traversal of binary tree
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

#utility function to create a new binary tree node
def newnode(data):
    temp=Node(0)
    temp.data=data
    temp.left=None
    temp.right=None
