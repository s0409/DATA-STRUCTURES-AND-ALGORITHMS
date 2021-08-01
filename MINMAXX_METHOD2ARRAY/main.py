import array
def getMinMax(low,high,arr):
    arr_max=arr[low]
    arr_min=arr[low]

    # if there is only one element
    if low==high:
        arr_max=arr[low]
        arr_min=arr[low]

        return (arr_min,arr_max)
    #if there is only two element
    elif high==low+1:
        if  arr[low]>arr[high]:
            arr_max=arr[low]
            arr_min=arr[high]
        else:
            arr_max=arr[high]
            arr_min=arr[low]
        return (arr_max,arr_min)
    else:

        #if there is more than two elements
        mid=int((low+high)/2)
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid+1,high ,arr)

    return (max(arr_max1,arr_max2),min(arr_min1,arr_min2))
#driver code
arr=[1000,11,445,1,330,3000]
high=len(arr)-1
low=0
arr_max, arr_min=getMinMax(low,high,arr)
print("minimum:",arr_min)
print("maximum:",arr_max)

