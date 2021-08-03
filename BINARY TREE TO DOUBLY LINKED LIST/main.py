#function to convert binary tree to DLL using inorder traversal
def fixprevptr(root):
    if root is not None:
        fixprevptr(root.left)
        root.left=fixprevptr.pre
        fixprevptr.pre=root
        fixprevptr(root.right)

#function to change right pointers to work as next pointers

def nextptr(root):
    prev=None
    #right most node in tree or last node in DLL
    while root and root.right !=None:
        root=root.right
    while root and root.left !=None:
        prev=root
        root=root.left
        root.right=prev
    return root

def binarytoDLL(root):
    fixprevptr.pre=None
    fixprevptr(root)
    return nextptr(root) 
