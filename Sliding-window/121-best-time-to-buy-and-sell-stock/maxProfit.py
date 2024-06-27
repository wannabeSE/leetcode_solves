def maxProfit(prices: list) ->int: 
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            currP = prices[r] - prices[l]
            maxP = max(maxP, currP)
        else: 
            l = r #? reducing time complexity as it will be the new minimum point to buy
        r += 1        
    return maxP
print(maxProfit([7,1,5,3,6,4]))
