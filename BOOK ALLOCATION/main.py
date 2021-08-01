#utility function to check the current minimum is feasible or not
def ispossible(arr,n,m,curr_min):
    student=1
    curr_sum=0
    #iterate over all books
    for i in range(n):
        #check if current number of page are
        #greater than curr_min that means
        #we will get result after mid number of pages
        if arr[i]>curr_min:
            return False
        #count how many student are required
        if curr_sum+arr[i]>curr_min:
            student+=1
            curr_sum+=arr[i]
            #if student are greater
            if student>m:
                return False
        else:
            curr_sum+=arr[i]
    return True
def findpages(arr,n,m):
    sum=0
    if n<m:
        return -1
    for i in range(n):
        sum+=arr[i]
    start=0
    end=sum
    res=""
    while start<=end:
        mid=(start+end)//2
        if ispossible(arr,n,m,mid):
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res


arr = [12, 34, 67, 90]
n = len(arr)
m = 2  # No. of students

print("Minimum number of pages = ",
      findpages(arr, n, m))