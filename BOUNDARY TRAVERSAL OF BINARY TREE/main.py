def printleaves(root,res):
    #this function is similar to inorder traversal
    if root is not None:
        printleaves(root.left,res)
        if root.left is None and root.right is None:
            res.append(root.data)
        printleaves(root.right,res)

def printrightboundary(root,res):
    if root is not None:
        if root.right is not None:
            printrightboundary(root.right,res)
            res.append(root.data)
        elif root.left is not None:
            printrightboundary(root.left,res)
            res.append(root.data)

def printleftboundary(root,res):
    if root is not None:
        if root.left is not None:
            res.append(root.data)
            printleftboundary(root.left,res)
        elif root.right is not None:
            res.append(root.data)
            printleftboundary(root.right,res)

def printboundary(root):
    res=[]
    if root is not None:
        res.append(root.data)
        printleftboundary(root.left,res)
        printleaves(root,res)
        printrightboundary(root.right,res)
    return res
#driver code runs here
if __name__ == "__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=printboundary(s)
        obj=Solution()
        res=obj.printboundary(root)
        for i in res:
            print(i,end =" ")
        print('')
        
