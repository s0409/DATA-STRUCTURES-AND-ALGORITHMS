def compute(head):
    curr=head
    prev=None
    next=None
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev

    current=head
    maxNode=head
    temp=None

    while current is not None and current.next is not None:
        if current.next.data<maxNode.data:
            temp=current.next
            current.next=temp.next
        else:
            current=current.next
            maxNode=current
    curr=head
    prev=None
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
