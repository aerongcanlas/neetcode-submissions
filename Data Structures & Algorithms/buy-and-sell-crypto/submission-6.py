class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy , maxProfit = prices[0], 0

        for price in prices:
            minBuy  = min(minBuy, price)
            maxProfit = max(maxProfit, price - minBuy )
        
        return maxProfit