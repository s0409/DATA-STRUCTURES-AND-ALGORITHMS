class Solution:
    def productexceptself(self,arr,n):
        #base case
        if n==1:
            return [1]
        i,temp=1,1
        #allocate memory for product array
        prod=[1 for i in range(n)]
        #initialize product array as 1
        #in this loop temp variable contains product of
        #elements on left side excluding arr[i]
        for i in range(n):
            prod[i]*=temp
            temp*=arr[i]
        #initialize temp to 1 for product on right side
        temp=1
        #in this loop temp variable contains product of
        #element on right side excluding arr[i]
        for i in range(n-1,-1,-1):
            prod[i]*=temp
            temp*=arr[i]
        return prod
if __name__=="__main__":
    arr=[10,3,5,6,2]
    n=len(arr)
    ob=Solution()
    print(ob.productexceptself(arr,n))