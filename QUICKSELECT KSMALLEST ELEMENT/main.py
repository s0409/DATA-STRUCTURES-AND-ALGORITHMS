"""#implementation of quick select

#makes use of standard partion process of quicksort()
#it considers the last element as pivot
#and moves all the smaller elements to left og
#it and greater elements to right

def partition(arr,l,r):

    x=arr[r]
    i=l
    for j in range(l,r):

        if arr[j]<=x:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1

    arr[i],arr[r]=arr[r],arr[i]
    return i

#find the kth position (of the sorted array)
#in a given unsorted array i.e this function can be used to find both
#kth largest and smalllest element in array
#ASSUMPTION: all elements in arr[]  are  distinct
def Kthsmallest(arr, l, r, k):
    #if k is smaller then number of elements in array
    if (k>0 and k<=r-l+1):
        #partion the array around the last element
        #and get position of pivot element in sorted array
        pivotIndex=partition(arr,l,r)

        #if postion is same
        if (pivotIndex-l==k-1):
            return arr[pivotIndex]

        #if position of element is more,recur for left sub array
        if (pivotIndex-l>k-1):
            return Kthsmallest(arr,l,pivotIndex-1,k)
        #else recur for right sub array
        return Kthsmallest(arr,pivotIndex+1,r,k-pivotIndex+l-1)


arr=[10,4,5,8,6,11,26]
n=len(arr)
k=3
print(Kthsmallest(arr,0,n-1,k))"""
def partition(arr,left,right):
    x=arr[right]
    i=left
    for j in range(left,right):
        if arr[j]<=x:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1

    arr[i],arr[right]=arr[right],arr[i]
    return i

def kthsmallest(arr,left,right,k):
    if (k>0 and k<=right-left+1):
        pivot=partition(arr,left,right)
    if (pivot-left==k-1):
        return arr[pivot]
    if (pivot-left>k-1):
        return kthsmallest(arr,left,pivot-1,k)

    return kthsmallest(arr,pivot+1,right,k-pivot+left-1)

arr=[1,2,5,6,8,55,4]
n=len(arr)
k=3
arr=kthsmallest(arr,0,n-1,k)



