def MERGELIST(n1,n2):
    ret=None
    #compare data in both list and storing the smaller in result
    #and recursively callingthe merge list function
    if n2.data<n1.data:
        ret=n2
        n2=n2.next
    else:
        ret=n1
        n1=n1.next
    tail=ret
    while n1 is not None and n2 is not None:
        if n2.data<n1.data:
            tail.next=n2
            tail=n2
            n2=n2.next
        else:
            tail.next=n1
            tail=n1
            n1=n1.next
    if n1:
        tail.next=n1
    if n2:
        tail.next=n2
    #returning the resultant list
    return ret
def mergelistss(arr,k):
    N=K
    last=N-1
    while i<j:
        arr[i]=MERGELIST(arr[i],arr[j])
        i+=1
        j-=1
        if i>=j:
            last=j
    return arr[0]
 
