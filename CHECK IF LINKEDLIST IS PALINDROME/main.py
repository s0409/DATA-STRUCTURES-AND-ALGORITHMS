def ispalindrome(head):
    slow_ptr=head
    fast_ptr=head
    prev_slow=head
    midNode=None
    res=True

    if head!=None and head.next!=None:
        while fast_ptr!=None and fast_ptr.next!=None:
            fast_ptr=fast_ptr.next.next
            prev_slow=slow_ptr
            slow_ptr=slow_ptr.next
        if fast_ptr!=None:
            midNode=slow_ptr
            slow_ptr=slow_ptr.next

        second_half=slow_ptr
        prev_slow.next=None

        #reverse the second half
        second_half=reverse(second_half)

        res=comparelist(head,second_half)

        second_half=reverse(second_half)
        if midNode!=None:
            #node not part of first half and second half
            prev_slow.next=midNode
            midNode.next=second_half
        else:
            prev_slow.next=second_half
    return res
def reverse(second_half):
    prev=None
    curr=head
    next=None
    while curr!=None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    second_half=prev
    return second_half
def comaparelist(head1,head2):
    temp1=head1
    temp2=head2
    while temp1 and temp2:
        if temp1.data==temp2.data:
            temp1=temp1.next
            temp2=temp2.next
        else:
            return 0
    if temp1==None and temp2==None:
        return 1
    return 0


