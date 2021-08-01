def sequence(arr,input):
    n=len(input)
    output=""
    for i in range(n):
        #3checking for space
        if input[i]==" ":
            output=output+"0"
        else:
            #calculate index for each character
            position=ord(input[i])-ord("A")
            output=output+arr[position]
    return output
str=["2","22","222",
     "3","33","333",
     "4","44","444",
     "5","55","555",
     "6","66","666",
     "7","77","777","7777",
     "8","88","888",
     "9","99","999","9999"]
input="MUSKAANSHIVAM"
print(sequence(str,input))