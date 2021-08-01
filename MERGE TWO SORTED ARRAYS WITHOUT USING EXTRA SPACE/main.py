import array
def Gap(gap):
    if gap<=1:
        return 0
    return (gap//2)+(gap%2)
def merge(arr1,arr2,n,m):
    gap=n+m
    gap=Gap(gap)
    while gap>0:
        i=0
        while i+gap<n:
            if arr1[i]>arr1[i+gap]:
                arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
            i+=1
            j=gap-n if gap>n else 0

            while i<n and j<m:
                if arr1[i]>arr2[j]:
                    arr1[i],arr2[j]=arr2[j],arr1[i]
                i+=1
                j+=1
            if j<m:
               j=0
               while j+gap<m:
                   if arr2[j]>arr2[j+gap]:
                       arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
                   j+=1
            gap=Gap(gap)

arr1=[1,2,3,4]
arr2=[5,6,7,8]
n=len(arr1)
m=len(arr2)
merge(arr1,arr2,n,m)




