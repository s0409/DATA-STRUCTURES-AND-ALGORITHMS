def leftview(result,node,level):
    global max_level
    if node==None:
        return
    #if this is the first node of its level it is in left view
    if max_level<level:
        #storing data of current node
        result.append(node.data)
        max_level=level
    leftview(result,node.left,level+1)
    leftview(result,node.rightlevel+1)
#fumction to return a list containing element
def leftView(root):
    global max_level
    max_level=0
    result=[]
    leftview(result,root,1)
    return result

