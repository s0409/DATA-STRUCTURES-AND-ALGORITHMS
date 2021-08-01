#function to find middle element in linkedlist
def findmiddle(head):
    if head==None:
        return head
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow.data
