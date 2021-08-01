def isomorphic(str1,str2):
    m=len(str1)
    n=len(str2)
    MAX_CHARS=256

    #if len of str1 and str2 are not same
    if m!=n:
        return False
    #to mark visited characters in strings
    marked=[False]*MAX_CHARS

    #to store mapping of every characters from str1 to
    #str 2
    map=[-1]*MAX_CHARS

    #process all characters one by one
    for i in range(n):
        #if current character of str1 is seen first time in it
        if map[ord(str1[i])]==-1:
            #if current character of str2 is already see
            #one to one mappin is not possible
            if marked[ord(str2[i])]==True:
                return False
            #mark current character of str2 as visited
            marked[ord(str2[i])]=True
            #store mappings of currents character
            map[ord(str1[i])]=str2[i]

        #if this is not first appearance of current
        #character in str1 then check if previous
        #appearance mapped to same character of str 2
        elif map[ord(str1[i])]!=str2[i]:
            return False
    return True
str1="aab"
str2="xxy"
print(isomorphic(str1,str2))

