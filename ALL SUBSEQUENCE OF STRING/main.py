#use pick and dont pick concept
def subsequence(str,substr=""):
     #to store subsequence

    if len(str)==0:
        print(substr,end=" ")
        return
    #we start adding 1st character in string
    subsequence(str[:-1],substr+str[-1])
    #Not adding first character in stringbeacause
    #the concept of subsequence either character
    #will present or not
    subsequence(str[:-1],substr)
    return

str='abc'
subsequence(str)
