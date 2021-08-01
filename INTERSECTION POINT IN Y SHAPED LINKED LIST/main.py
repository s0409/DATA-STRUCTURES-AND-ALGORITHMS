#function for finding intersection point of y shaped linked list
def intersection(head1,head2):
    ptr1=head1
    ptr=head2
    c1=0
    c2=0
    while ptr1:
        c1+=1
        ptr1=ptr1.next
    while ptr2:
        c2+=1
        ptr2=ptr2.next
    ptr1=head1
    ptr2=head2
    diff = abs(c1-c2)
    if c1>c2:
        for i in range(diff):
            ptr1=ptr1.next
    elif ptr2>ptr1:
        for i in range(diff):
            ptr2=ptr.next
    while ptr1!=ptr2:
        ptr1=ptr1.next
        ptr2=ptr2.next
    if ptr1:
        return ptr1.data
    return -1
