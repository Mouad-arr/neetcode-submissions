class Solution:
    def integerBreak(self, n: int) -> int:
        memo={}
        def dfs(num):
            if num in memo : 
                return memo[num]
            if num == 1:
                return 1
            res = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res, val)
            memo[num]=res
            return res
        return dfs(n)