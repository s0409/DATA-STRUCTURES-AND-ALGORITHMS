#function to return ksmaleest element in given array
def KSmallest(arr,n,k):

    #sort the given array
    arr.sort()

    #return kth element in the sorted array
    return arr[k-1]

#driver code
if __name__=="__main__":
    arr=[12,3,5,7,19]
    #size of array
    n=len(arr)
    k=2 #can also be taken as input
    print(KSmallest(arr,n,k))