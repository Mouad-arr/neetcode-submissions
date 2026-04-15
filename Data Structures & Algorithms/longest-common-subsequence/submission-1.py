class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        d={}
        def dfs(i,j):
            if (i,j) in d:
                return d[(i,j)]
            if i==n or j == m:
                return 0
            if text1[i]==text2[j]:
                res = 1+dfs(i+1,j+1)
                d[(i,j)]=res
                return res
            else:
                res= max(dfs(i+1,j),dfs(i,j+1))
                d[(i,j)]=res
                return res
        return dfs(0,0)