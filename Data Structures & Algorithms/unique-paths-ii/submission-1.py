class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp={}
        def dfs(i,j) :
            if (i,j) in dp :
                return dp[(i,j)]
            if i<0 or j<0 or i>=m or j>=n :
                return 0
            elif obstacleGrid[i][j]==1 :
                return 0
            elif i==m-1 and j==n-1 :
                return 1
            else :
                res= dfs(i,j+1)+dfs(i+1,j)
                dp[(i,j)]=res
                return res
        return dfs(0,0)