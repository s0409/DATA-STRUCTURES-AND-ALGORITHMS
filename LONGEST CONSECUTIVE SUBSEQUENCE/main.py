def longestsub(arr,n):
    #create hash
    s=set()
    ans=0
    #insert all elements to hash
    for ele in arr:
        s.add(ele)
        #look for arr[i]-1
    for i in range(n):

        if arr[i]-1 not in s:
            j=arr[i]
            while j in s:
                j+=1
            ans=max(ans,j-arr[i])
    return ans
#driver code
if __name__=="__main__":
    arr=[1,3,5,9,8,4,2]
    n=len(arr)
    print(longestsub(arr,n))