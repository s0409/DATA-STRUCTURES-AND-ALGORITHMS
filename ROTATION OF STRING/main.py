def rotation(string1,string2):


    #check if sizes of two strings are same
    if size1!=size2:
        return 0
    #create a pattern string by joining string1+string2
    temp=string1+string2
    if temp.count(string2):
        return 1
    else:
        return 0
#driver code runs here
string1="mypencil"
string2="encilmyp"

if rotation(string1,string2):
    print("yes")
else:
    print("no")