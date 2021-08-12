class Item:
    def __init__(self,val,W):
        self.value=val
        self.weight=W

class Solution:
    #function to get the maximum total value in the knapsack
    def fractionalknapsack(self,W,Items,n):

        #taking variables for current weight in knapsack
        curr_weight=0
        curr_val=0

        #sorting items on basis of value/weight ratio
        Items=sorted(Items,key=lambda x:(x.value/x.weight),reverse=True)

        #iterating over all the items.
        for i in range(n):
            if curr_weight+Items[i].weight<=W:
                curr_weight += Items[i].weight
            else:
                accomodate=W-curr_weight
                value_added = Items[i].value*(accomodate/Items[i].weight)
                curr_val += value_added
                break
        return curr_val
t=int(input())
for cases in range(t):
    n,W=map(int,input().strip().split())
    info=list(map(int,input().strip().split()))
    Items=[Items(0,0) for i in range(n)]
    for i in range(n):
        Items[i].value=info[2*i]
        Items[i].weight=info[2*i+1]
    ob=Solution()
    print("%.2f" %ob.fractionalknapsack(W,Items,n))




