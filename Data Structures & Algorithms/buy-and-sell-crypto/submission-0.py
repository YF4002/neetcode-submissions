class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1 #two pointers: left=buy ; right=sell
        maxprofit = 0 #maximum profit possible

        while r < len(prices): #keep iterating while right pointer has not pass the end of prices.
            #is it profitable?
            if prices[l] < prices[r]: #if left price is less than right / if buying is less than selling
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit) #check the maximum profit out of the two max(maxprofit, profit)
            else:
                l = r #shift left pointer to right because we want it to be at the minimum price
            r +=1

        return maxprofit
