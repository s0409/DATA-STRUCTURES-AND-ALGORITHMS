def secondRep(arr,n):
    #store all the words with occurences
    occ={}
    for i in range(n):
        occ[arr[i]]=occ.get(arr[i],0)+1

    #find the second largest occurence
    first_max=-10**8
    sec_max=-10**8
    for var in occ:
        if occ[var]>first_max:
            sec_max=first_max
            first_max=occ[var]
        elif occ[var]>sec_max and occ[var]!=first_max:
            sec_max=occ[var]
    for var in occ:
        if occ[var]==sec_max:
            return var

arr= [ "ccc", "aaa", "ccc",
    "ddd", "aaa", "aaa" ]
n=len(arr)
print(secondRep(arr,n))