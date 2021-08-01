#text
#pattern
#prime number
#number of character in input alphabet
d=256
def search(pat,text,q):
    M=len(pat)
    N=len(text)
    i=0
    j=0
    p=0
    t=0
    h=1
    #the value of h would be h=(h*d)%q
    for i in range(M-1):
        h=(h*d)%q
    #calculate the hash value of pattern and first window
    #of text
    for i in range(M):
        p=(d*p+ord(pat[i]))%q
        t=(d*t+ord(text[i]))%q
    #slide the pattern over text one by one
    for i in range(N-M+1):
        if p==t:
            #check for characters one by one
            for j in range(M):
                if text[i+j]!=pat[j]:
                    break
                else:
                    j+=1
                if j==M:
                    print("pattern found " +str(i))
        #calculate the hash value for next window of text
        if i<N-M:
            t=(d*(t-ord(text[i])*h)+ord(text[i+M]))%q
            #we might get negative values of t convert it in to positive
            if t<0:
                t=t+q
text="geeks for geeks"
pat="geeks"
q=101
search(pat,text,q)

