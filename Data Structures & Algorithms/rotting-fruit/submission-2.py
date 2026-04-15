class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        freshFruit=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2 :
                    q.append((i,j))
                elif grid[i][j]==1:
                    freshFruit+=1
        if freshFruit == 0 :
            return 0
                
        minutes =  0
        while q and freshFruit != 0:
            l=len(q)
            for _ in range(l):
                x,y=q.popleft()
                for dx,dy in directions :
                    i,j=x+dx,y+dy
                    if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0 or grid[i][j]==2:
                        continue
                    freshFruit-=1
                    grid[i][j]=2
                    q.append((i,j))
            minutes+=1
        return minutes if freshFruit==0 else -1