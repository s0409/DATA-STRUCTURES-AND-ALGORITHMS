def swapCount(S):
    chars=S

    #store total number of left and right brackets encountered
    countLeft=0
    countRight=0

    #swap stores the number of swaps
    #required imbalance maintains the
    #number of imbalance pairs
    swap=0
    imbalance=0
    for i  in range(len(chars)):
        if chars[i]=="[":

        #increment count for left bracket
           countLeft+=1
           if imbalance>0:
            #swap count is the last swap count+
            #total number imbalance brackets
                swap+=imbalance

            #imbalance dec by 1 as it solve only one imbalance
            #of left and right
                imbalance-=1
        elif chars[i]=="]":
            countRight+=1
            imbalance=countRight-countLeft
    return swap
S="[[][]]"
print(swapCount(S))