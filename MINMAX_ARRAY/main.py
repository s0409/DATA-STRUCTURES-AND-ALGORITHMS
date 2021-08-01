import array
class pair:
    def __init__(self):
        self.min=0
        self.max=0
def getMinMax(arr:list,n:int) -> pair:
    minmax=pair

    # if there is only one element
    if n==1:
        minmax.max=arr[0]
        minmax.min=arr[0]
        return minmax

    # if there are more than one element in array
    if arr[0]>arr[1]:
        minmax.max=arr[0]
        minmax.min=arr[1]

    else:
        minmax.max=arr[1]
        minmax.min=arr[0]

    for i in range(2,n):
        if arr[i]>minmax.max:
            minmax.max=arr[i]
        elif arr[i]<minmax.min:
            minmax.min=arr[i]

    return minmax
if __name__=="__main__":
    arr=[123,3456,56,2,0,1]
    arr_size=6
    minmax=getMinMax(arr,arr_size)
    print(minmax.min)
    print(minmax.max)