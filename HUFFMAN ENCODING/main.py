from heapq import heappush,heappop,heapify
class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def __lt__(self, other):
        return False
class Solution:
    def huffmanCodes(self,S,F,N):
        def traverse(node,p,ans):
            if not node.left and not node.right:
                ans.append(p)
            traverse(node.left,p+'0',ans)
            traverse(node.right,p+'1',ans)
        heap=[]
        for i in range(N):
            heap.append([F[i],Tree(S[i])])
            heapify(heap)
            while len(heap)!=1:
                x=heappop(heap)
                y=heappop(heap)
                z=Tree(x[0]+y[0])
                z.left=x[1]
                z.right=y[1]
                heappush(heap,[x[0]+y[0],z])
            root=heap[0][1]
            ans=[]
            traverse(root," ",ans)
            return ans
#driver code
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        S=input()
        N=len(S)
        F=[int(x) for x in input().split()]
        ob=Solution()
        ans=ob.huffmanCodes(S,F,N)
        for i in ans :
            print(i,end=" ")
        print()

