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
            # j=i+1
            d[i]=0
            # while j<n and prices[i] < prices[j]:
            #     if j+1 < n and prices[i]<prices[j+1]:
            #         r=max(prices[j]-prices[i]+max(dfs(j+2),dfs(j+3)),prices[j+1]-prices[i]+max(dfs(j+3),dfs(j+4)))
            #         d[i]=max(r,d[i])
            #     elif j < n:
            #         r=prices[j]-prices[i]+max(dfs(j+2),dfs(j+3))
            #         d[i]=max(r,d[i])
            #     j+=1
            for j in range(i+1,n):
                d[i]=max(d[i],(prices[j]-prices[i])+dfs(j+2))
            return d[i]
        for i in range(n):
            res = max(res,dfs(i))
        return res
        