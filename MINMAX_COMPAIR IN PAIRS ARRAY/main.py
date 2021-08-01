import array
def getMinMax(arr):
    n=len(arr)

    #if array has even number of element then initialize the
    #first two element as min and max
    if (n%2==0):
        maxi=max(arr[0],arr[1])
        mini=min(arr[0],arr[1])

        #set the starting inndex for loop
        i=2
    #if the array holds odd number of element then initialize the
    #first element as minimum and maximum
    else:
        maxi=mini=arr[0]

        #set the starting index for loop
        i=1

    #in the whhile loop ,pick elements in pair
    #compare the pair with max and min so far
    while(i<n-1):
         if arr[i]<arr[i+1]:
               maxi=max(maxi,arr[i+1])
               mini=min(mini,arr[i])
         else:
             maxi=max(maxi,arr[i])
             mini=min(mini,arr[i+1])
         #increment the index by 2 as two
         #as two elements are processed in a loop

         i+=2

    return (maxi,mini)
#driver code
if __name__=="__main__":
    arr=[1000,11,445,1,330,3000]
    maxi,mini=getMinMax(arr)
    print(maxi)
    print(mini)
