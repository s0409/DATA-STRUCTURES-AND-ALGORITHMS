def smallWindow(s,p):
    #if len of s is less than len of p
    if len(p)>len(s):
        return -1
    #using hash table to store the count of characters
    s_hash=[0 for i in range(26)]
    p_hash=[0 for i in range(26)]

    #store the count of characters of p in p_hash
    for char in p:
        p_hash[ord(char)-ord('a')]+=1
    count=0
    start=0
    start_index=-1
    length=0
    min_length=1e10

    for i in range(len(s)):
        s_hash[ord(s[i])-ord('a')]+=1
        if (p_hash[ord(s[i])-ord('a')] !=0 and s_hash[ord(s[i])-ord('a')]<=p_hash[ord(s[i])-ord('a')]):
            count+=1
        #if all the characters are matched
        if count==len(p):
            #we try to minimize the window
            while (s_hash[ord(s[start])-ord('a')]>p_hash[ord(s[start])-ord('a')] or p_hash[ord(s[start])-ord('a')]==0):
                if (s_hash[ord(s[start])-ord('a')]>p_hash[ord(s[start])-ord('a')]):
                    s_hash[ord(s[start])-ord('a')]-=1
                    start+=1
                #update window size
                length=i-start+1
                if length<min_length:
                    start_index=start
                    min_length=length
    if start_index==-1:
        return "-1"
    else:
        return s[start_index:start_index+min_length]
s="this is a test string"
p="tist"
print(smallWindow(s,p))