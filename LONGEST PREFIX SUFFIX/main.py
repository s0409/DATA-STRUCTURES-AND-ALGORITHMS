def lps(str):
    n=len(str)
    lps=[0]*n
    j=0
    i=1
    while i<n:
        if str[i]==str[j]:
            lps[i]=j+1
            j+=1
            i+=1
        else:
            if j==0:
                i+=1
            else:
                j=lps[j-1]
    return lps[-1]
str="abcab"
print(lps(str))
