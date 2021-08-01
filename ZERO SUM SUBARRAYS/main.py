class Solution:
    def findsubarray(self,arr, n):
        count = 0
        hashmap = {}
        ans = []
        sum1 = 0
        # iterating over the array
        for i in range(n):
           #storing prefix sum
           sum1 += arr[i]
           # if prefix sum is zero that means we get a subarray with sum zero
           if sum1 == 0:
              ans.append((0, i))
              # incrementing the counter
              count += 1
           al = []
           # if prefix sum is already present in map then it is repeated
           # which means there is a subarray whose summation is 0
           if sum1 in hashmap:
              al = hashmap.get(sum1)
              for var in range(len(al)):
                   ans.append((al[var] + 1, i))
                   count += 1
           al.append(i)
           # storing the count of map prefix sum obtained in map
           hashmap[sum1] = al
        return count
arr = [0, 0, 5, 5, 0, 0]
n = len(arr)
ob=Solution()
print(ob.findsubarray(arr, n))




