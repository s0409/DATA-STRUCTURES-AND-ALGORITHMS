def productsubarray(arr,n):
    max_ending_here=1
    min_ending_here=1
    max_so_far=0
    for i in range(n):
        if arr[i]>n:
            max_ending_here=max_ending_here*arr[i]
            min_ending_here=min(min_ending_here*arr[i],1)
        elif arr[i]==0:
            max_ending_here=1
            min_ending_here=1
        else:
            temp=max_ending_here
            max_ending_here=max(min_ending_here*arr[i],1)
            min_ending_here=temp*arr[i]
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
        if max_so_far==0:
            return 0
    return max_so_far
arr=[1,-2,-3,0,7,-8,-2]
n=len(arr)
print(productsubarray(arr,n))
