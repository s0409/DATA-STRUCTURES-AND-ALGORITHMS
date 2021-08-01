def maxProfit(price,n):
    #create profit array
    profit=[0]*n
    #get max profit by one transaction
    max_price=price[n-1]
    for i in range(n-2,0,-1):
        if price[i]>max_price:
            max_price=price[i]
        #we can get profit by taking maximum of previous maximum
        #profit[i+1]
        profit[i]=max(profit[i+1],max_price-price[i])
    #get maximum profit by two transaction
    min_price=price[0]
    for i in range(1,n):
        if price[i]<min_price:
            min_price=price[i]
        #maximum profit is maximum of previous maximum
        profit[i]=max(profit[i-1],profit[i]+(price[i]-min_price))
        result=profit[n-1]
    return result



price = [2, 30, 15, 10, 8, 25, 80]
print("Maximum profit is", maxProfit(price, len(price)))


