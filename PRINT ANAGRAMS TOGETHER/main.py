from collections import defaultdict
def anagram(arr,n):
    d=defaultdict(list)
    #traverse
    for i,e in enumerate(arr):
        e=str(sorted(e))
        d[e].append(arr[i])
    res=[]
    for l in d.values():
        res.append(l)
    return res
arr=["act","god","cat","dog","tac"]
n=len(arr)
print(anagram(arr,n))