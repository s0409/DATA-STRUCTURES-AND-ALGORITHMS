def find_max(arr):
    incl=0
    excl=0
    for i in arr:
        #current max element i(No ternary in python)
        new_excl=excl if excl>incl else incl
        #current max including i
        incl=excl+i
        excl=new_excl
    return excl if excl>incl else incl
arr=[5,5,10,100,10,5]
print(find_max(arr))