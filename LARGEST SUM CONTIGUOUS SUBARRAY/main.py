#kadane's algorithm
"""initialize
max_so_far=0
max_ending_here=0
==>>loop for each element in the array
1. max_ending_here=max_ending_here+a[i]
2.if (max_so_far<max_ending_here):
     max_so_far=max_ending_here
3.if (max_ending_here<0):
     max_ending_here=0
return max_so_far"""
import array
def maximumsubarraySum(arr,size):
    max_so_far=arr[0]
    max_ending_here=0
    for i in range(0,size):
        max_ending_here=max_ending_here+arr[i]
        if (max_so_far<max_ending_here):
            max_so_far=max_ending_here
        elif max_ending_here<0:
            max_ending_here=0
    return max_so_far
a = [-2,1,-3,1,-1,2,1,-5,4]
print(maximumsubarraySum(a,len(a)))

