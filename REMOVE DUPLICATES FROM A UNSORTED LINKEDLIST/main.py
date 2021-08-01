def removedupllicate(head):
    if head is None and head.next is None:
        return
    hash=set()
    temp=head
    hash.add(head.data)
    while temp.next is not None:
        if temp.next.data in hash:
            temp.next=temp.next.next
        else:
            hash.add(temp.next.data)
            temp=temp.next
    return head
