class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)== 1 :
            return 0
        m=0
        for i in range(len(prices)-1,0,-1) :
            for j in range(i-1,-1,-1) :
                m=max(m,prices[i]-prices[j])
        return m