#function to return diameter of tree


def utility(root):
    dia=0
    if root == None:
        return 0
    global dia

    l=self.utility(root.left)
    r=self.utility(root.right)

    dia=max(dia,l+r+1)
    return 1+max(l,r)
def diameter(root):
    global dia
    dia=0
    self.utility(root)
    return dia
