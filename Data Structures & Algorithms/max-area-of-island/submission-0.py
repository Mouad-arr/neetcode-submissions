class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        ROWS,COLS=len(grid),len(grid[0])
        def dfs(i,j) :
            if i<0 or j<0 or i>=ROWS or j>= COLS or grid[i][j]==0 :
                return 0
            grid[i][j]=0
            return 1 + dfs(i+1,j) + dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)


        for i in range(ROWS) :
            for j in range(COLS) :
                if grid[i][j] == 1 : 
                    maxArea=max(dfs(i,j),maxArea)
        return maxArea