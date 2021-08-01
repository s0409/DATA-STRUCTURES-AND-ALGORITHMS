def removeDuplicate(S):
    stack=[]
    for i in range(len(S)):
        if (stack and stack[-1]!=S[i]) or not stack:
            stack.append(S[i])
    res=""
    while stack:
        res+=stack.pop()
    return res[::-1]
S="aabb"

print(removeDuplicate(S))