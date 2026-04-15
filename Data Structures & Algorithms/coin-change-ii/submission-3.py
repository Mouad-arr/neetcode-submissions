class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n=len(coins)
        d={}
        def dfs(i,a):
            if (i,a) in d:
                return d[(i,a)]
            if a==0:
                return 1
            if i>=n:
                return 0
            res=0
            if a>=coins[i]:
                res = dfs(i+1,a)
                res+=dfs(i,a-coins[i])
            d[(i,a)]=res
            return res
        return dfs(0,amount)        