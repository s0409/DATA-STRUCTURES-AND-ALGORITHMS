def minflip(S):
    n=len(S)
    count=0
    for i in range(0,n):
        #if there is one at even index
        if i%2==0 and S[i]=="1":
            count+=1
        #if there is zero at odd index
        if i%2==1 and S[i]=="0":
            count+=1
    return min(count,n-count)
S = "1100"
print(minflip(S))