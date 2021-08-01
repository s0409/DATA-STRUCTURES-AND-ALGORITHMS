class Node:
    #a utility fuction to create a new node
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def printlevelorder(root):
    #base case
    res=[]
    if root is None:
        return res
    queue=[]
    queue.append(root)
    while 1:
        n=len(queue)
        if n==0:
            break
        while(n>0):
            node=queue.pop(0)
            res.append(node.data)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            n-=1
    return res

