def copylist(head):
    curr=head
    while curr:
        next=curr.next
        dup=Node(curr.next)
        curr.next=dup
        dup.next=next
        curr=next
    curr=head
    while curr:
        if curr.arb:
            curr.next.arb=curr.arb.next
        curr=curr.next.next
    dummy=Node(-1)
    tail=dummy
    curr=head
    while curr:
        next=curr.next.next
        dup=curr.next
        tail.next=dup
        tail=dup
        curr.next=next
        curr=next
    return dummy.next

