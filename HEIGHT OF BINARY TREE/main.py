class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class Solution:
    def height(self,root):
        if root is None:
            return 0
        else:
            left=self.height(root.left)
            right=self.height(root.right)

            if left>right:
                return left+1
            else:
                return right+1
#Driver code runs here
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
ob=Solution()
print(ob.height(root))

