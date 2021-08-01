def ispalindrome(s):
    n=len(s)
    if n==1:
        return 1
    flag=0
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            flag="no"
            break
        else:
            flag="yes"
    return flag
s="121"
print(ispalindrome(s))
