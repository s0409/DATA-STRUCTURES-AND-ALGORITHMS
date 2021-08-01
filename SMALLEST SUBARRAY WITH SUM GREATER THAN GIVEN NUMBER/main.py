def small(arr,n,k):
    #initialize current sum and min length
    curr_sum=0
    min_len=n+1
    #initialize the starting and ending indices
    start=0
    end=0
    while end<n:
        while curr_sum<=k and end<n:
            curr_sum+=arr[end]
            end+=1
        while curr_sum>k and start<n:
            if end-start<min_len:
                min_len=end-start
            curr_sum-=arr[start]
            start+=1
    return min_len
arr=[1,4,45,6,10,19]
n=len(arr)
k=51
print(small(arr,n,k))