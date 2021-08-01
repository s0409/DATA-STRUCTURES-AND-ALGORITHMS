def iscircular(head):
    if head is None:
        return True
    node = head.next
    i = 0
    while node is not None and node is not head:
        i = i+1
        node = node.next
    return node == head
