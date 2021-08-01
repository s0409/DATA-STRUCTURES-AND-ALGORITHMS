class Height:
    def __init__(self):
        self.height=0
def utility(root,height):

    lh=Height()
    rh=Height()

    if root is None:
        return True
    l=utility(root.left,lh)
    r=utility(root.right,rh)

    height.height=max(lh.height,rh.height)+1

    if abs(lh.height-rh.height)>=2:
        return False
    else:
        return l and r
def isBalanced(root):
    height=Height()
    return isBalanced(root,height)

