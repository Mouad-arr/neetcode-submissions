class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # output=-1
        # minutes=0
        # visited=[[False for _ in range(len(grid[0]))]for _ in range(len(grid))]
        # def dfs(i,j) :
        #     if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0  or visited[i][j] :
        #         return 
        #     visited[i][j]=True
        #     if grid[i][j] == 1 :
        #         grid[i][j]=2
        #     else:
        #         dfs(i+1,j)
        #         dfs(i-1,j)
        #         dfs(i,j+1)
        #         dfs(i,j-1)
        #     visited[i][j]=False
        # while True :
        #     initial=sum(row.count(2) for row in grid)
        #     for i in range(len(grid)) :
        #         for j in range(len(grid[0])):
        #             if grid[i][j]==2 :
        #                 dfs(i,j) 
        #     if initial == sum(row.count(2) for row in grid) :
        #         return output
        #     else :
        #         minutes+=1
        #         output=minutes


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