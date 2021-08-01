def nextpermutaion(arr,n):
    ind=0
    l=[]  #lastincluded
    l+=arr
    #finding peak of last ascending order
    for i in range(n-2,-1,-1):
        if l[i]<l[i+1]:
            ind=i
            break
    #check if the array is in descending order
    for i in range(n-1,ind,-1):
        if l[i]>l[ind]:
            l[i],l[ind]=l[ind],l[i]
            ind+=1
            break
    for i in range((n-ind)//2):
        l[i+ind],l[n-i-1]=l[n-i-1],l[i+ind]
    return l
arr=[1,2,3,6,5,4]
n=len(arr)
print(nextpermutaion(arr,n))
