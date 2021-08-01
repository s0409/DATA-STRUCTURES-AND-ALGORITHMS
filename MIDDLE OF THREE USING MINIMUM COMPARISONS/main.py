def middle(a,b,c):
    if ((a < b and b < c) or (c < b and b < a)):
        return b

        # Checking for a
    if ((b < a and a < c) or (c < a and a < b)):
        return a

    else:
        return c
a = 978
b= 518
c = 300
print(middle(a,b,c))