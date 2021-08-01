def longestpal(string):
    maxLength=1

    start=0
    n=len(string)

    low=0
    high=0
    #one by one consider every character as center point of
    #even and length palindrome
    for i in range(1,n):
        #find the longest even length palindrome with
        #center points as i-1 and i
        low=i-1
        high=i
        while low>=0 and high<n and string[low]==string[high]:
            if high-low+1>maxLength:
                start=low
                maxLength=high-low+1
            low-=1
            high+=1
        #fnd the longest odd length palindrome
        low=i-1
        high=i+1

        while low>=0 and high<n and string[low]==string[high]:
            if high-low+1>maxLength:
                start=low
                maxLength=high-low+1
            low-=1
            high+=1
    print("longest palindrome substring is :")
    print(string[start:start+maxLength])
    return maxLength
string="aaaabbaa"
print(longestpal(string))