class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = profit = 0
        sell = 1
        ans = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            
            else:
                profit = prices[sell] - prices[buy]

                ans = max(ans, profit)
                sell += 1

        return ans

        




#iterate through arr prices
# buy=0 sell= 1, profit = 0, ans = 0
#while sell < len(prices)
#if prices[sell] < prices[buy], buy = sell
#else profit = prices[sell] - prices[buy]
#ans = max(ans, profit), sell += 1
# return  ans