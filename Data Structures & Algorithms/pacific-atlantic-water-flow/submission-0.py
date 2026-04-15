class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        ROWS=len(heights)
        COLS=len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pacific=set()
        atlantic=set()
        def dfs(r,c,visited):
            visited.add((r,c))
            for dx,dy in directions :
                i,j=r+dx,c+dy
                if 0<=i<ROWS and 0<= j< COLS and (i,j) not in visited and heights[i][j]>= heights[r][c] :
                    dfs(i,j,visited)
                
        # Pacific
        for c in range(COLS):
            dfs(0, c, pacific)
        for r in range(ROWS):
            dfs(r, 0, pacific)

        # Atlantic
        for c in range(COLS):
            dfs(ROWS-1, c, atlantic)
        for r in range(ROWS):
            dfs(r, COLS-1, atlantic)
        return [list(X) for X in pacific if X in atlantic ]
