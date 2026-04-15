class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if len(prices)<=1 :
            return 0
        res = 0
        d={}
        def dfs(i):
            if i in d :
                return d[i]
            if i >= n-1 :
                return 0
            d[i]=0
            for j in range(i+1,n):
                d[i]=max(d[i],(prices[j]-prices[i])+dfs(j+2))
            return d[i]
        for i in range(n-1):
            res = max(res,dfs(i))
        return res
        