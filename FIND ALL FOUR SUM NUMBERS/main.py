def foursum(arr,n,k):
    n=len(arr)
    ans=[]
    if n<4:
        return ans
    arr.sort()
    for i in range(0,n-3):
        #current element is greater than k then no quadruplet can
        #be found
        if arr[i]>0 and arr[i]>k:
            break
        #removing duplicates
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                old_l=left
                old_r=right
                #calculate current sum
                sum=arr[i]+arr[j]+arr[left]+arr[right]
                if sum==k:
                    ans.append([arr[i],arr[j],arr[left],arr[right]])
                    #removing duplicates
                    while left<right and arr[left]==arr[old_l]:
                        left+=1
                    while left<right and arr[right]==arr[old_r]:
                        right-=1
                elif sum>k:
                    right-=1
                else:
                    left+=1
    return ans
arr=[10,2,3,4,5,7,8]
n=len(arr)
k=23
print(foursum(arr,n,k))
