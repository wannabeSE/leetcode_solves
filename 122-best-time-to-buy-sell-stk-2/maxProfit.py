class Solution:
    def f(self, i, buy, prices):
        if i == len(prices):
            return 0
        profit = 0
        if buy:
            profit = max(- prices[i] + self.f(i + 1, 0, prices), 0 + self.f(i + 1, 1, prices)) # -price cause sell - buy 
        else:
            profit = max(prices[i] + self.f(i + 1, 1, prices), 0 + self.f(i + 1, 0, prices))
        return profit
        
    def maxProfit(self, prices: list) -> int:
        
        return self.f(0, 1, prices) #! dp needed, will get back to it later.

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))