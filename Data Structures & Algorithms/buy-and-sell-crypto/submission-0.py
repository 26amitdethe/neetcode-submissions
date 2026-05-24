class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minn  = prices[0]
        i=1
        while i<len(prices):
            if prices[i]<minn:
                minn = prices[i]
            if profit<prices[i]-minn:
                profit = prices[i]-minn
            i+=1
        return profit