class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n) :
                if grid[i][j]==0 :
                    q.append((i,j))
        while q : 
            x,y=q.popleft()
            for dx,dy in directions :
                ni=x+dx
                nj=y+dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[x][y] + 1:
                    grid[ni][nj]= grid[x][y] + 1
                    q.append((ni,nj))
        
