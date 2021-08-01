import array
def sort012(arr,arr_size):
    low=0
    mid=0
    high=arr_size-1

    while(mid<=high):
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1
        elif (arr[mid]==1):
            mid=mid+1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1

    return arr

#driver code
arr=[1,0,2,2,0,1,2,2,2,1,1,1,0]
arr_size=len(arr)
arr=sort012(arr,arr_size)
print(arr)
