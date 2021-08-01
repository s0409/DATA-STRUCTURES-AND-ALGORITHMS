#function to merge two halves of the given linkedlist using merge sort
def splitlist(a,b):
    result=None

    #base case
    if a==None:
        return b
    if b==None:
        return a

    #pick either a or b and recur
    if a.data<=b.data:
        result=a
        result.next=self.splitlist(a.next,b)
    else:
        result=b
        result.next=self.splitlist(a,b.next)
    return result
def mergesort(head):
    if head==None and head.next==None:
        return head
    #get middle of list
    middle=self.getmiddle(head)
    nexttomiddle=middle.next
    middle.next=None


    #apply merge sort on left side
    left=self.mergesort(head)
    #apply on right side
    right=self.mergesort(nexttomiddle)
    #merge the left and right list
    sortedlist=self.splitlist(left,right)
    return sortedlist
def getmiddle(head):
    if head==None:
        return head
    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow
