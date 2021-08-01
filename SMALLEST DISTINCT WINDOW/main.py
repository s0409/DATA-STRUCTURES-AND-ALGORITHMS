from collections import defaultdict
MAX_CHARS=256
def findSubString(str):
    n=len(str)
    #count all distinct characters
    dist_count=len(set([x for x in str]))
    curr_count=defaultdict(lambda:0)
    count=0
    start=0
    min_len=n
    #maintain window of characters that contain all characters
    for j in range(n):
        curr_count[str[j]]+=1
        if curr_count[str[j]]==1:
            count+=1
        #characters occuring more than one time remove from starting
        #and also remove the useless characters
        if count==dist_count:
            while curr_count[str[start]]>1:
                if curr_count[str[start]]>1:
                    curr_count[str[start]]-=1
                start+=1

            #update the window size
            len_window=j-start+1
            if min_len>len_window:
                min_len=len_window
                start_index=start
    return (str[start_index:start_index+min_len])
strr="aabcbcdbca"
print(findSubString(strr))