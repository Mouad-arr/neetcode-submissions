class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        minBuy=prices[0]
        for price in prices :
            minBuy=min(minBuy,price)
            maxP=max(maxP,price - minBuy)
        return maxP
