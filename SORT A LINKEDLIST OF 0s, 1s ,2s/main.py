def segregate(head):
    count0=1
    count1=0
    count2=0
    temp=head
    while temp is not None:
        if temp.data==0:
            count0+=1
        elif temp.data==1:
            count1+=1
        elif temp.data==2:
            count2+=1
        temp=temp.next
    temp=head
    while temp is not None:
        if count0 !=0:
            temp.data=0
            count0-=1
        elif count1 !=0:
            temp.data=0
            count1-=1
        elif count2 !=0:
            temp.data=0
            count2-=1
        temp=temp.next
    return head



