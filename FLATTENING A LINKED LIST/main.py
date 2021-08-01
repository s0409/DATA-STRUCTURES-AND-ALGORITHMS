#function for flatten a linked list

def merge(a,b):
    if a is None:
        return b
    if b is None:
        return a
    result=None
    if a.data<b.data:
        result=a
        result.bottom=merge(a.bottom,b)
    else:
        result=b
        resilt.bottom=merge(a,b.bottom)
    return result

def flatten(root):
    if root is None or root.next is None:
        return root
    root.next=flatten(root.next)
    root=merge(root,root.next)
    return root
