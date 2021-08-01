"""import array
def cycle(arr,n,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1


    return arr
arr=[1,2,3,4,5]
n=len(arr)
print(cycle(arr,n,0,n-1))"""


def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];

    arr[0] = x;


# Driver function
arr = [1, 2, 3, 4, 5]
print("the given array is",arr)
n = len(arr)
print(rotate(arr,n))
print("rotated array is :")
for i in range(0, n):
    print(arr[i], end=' ')

rotate(arr, n)


