class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        memo={}
        def dfs(i):
            if i in memo :
                return memo[i]
            if i == len(s):
                return 0

            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = min(res, dfs(j + 1))

            memo[i]= res
            return res

        return dfs(0)