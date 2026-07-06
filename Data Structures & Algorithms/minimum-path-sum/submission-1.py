class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp={}
        def dfs(i,j,cur):
            if (i,j,cur) in dp:
                return dp[(i,j,cur)]
            if i>=n or j>=m :
                return float('inf')
            if i==n-1 and j==m-1 :
                return cur+grid[i][j]
            else:
                cur+=grid[i][j]
                res= min(dfs(i,j+1,cur),dfs(i+1,j,cur))
                dp[(i,j,cur-grid[i][j])]=res
                return res
        return dfs(0,0,0)