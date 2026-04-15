class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        ROWS,COLS = len(board),len(board[0])
        visited=[[False for _ in range(COLS)]for _ in range(ROWS)]

        def dfs(i,j) :
            visited[i][j]=True
            for dx,dy in directions :
                x,y=i+dx,j+dy
                if x<0 or y<0 or x>=ROWS or y>=COLS :
                    visited[i][j]=False
                    return False
                if board[x][y]=="O" and not visited[x][y] :
                    if not dfs(x,y) :
                        visited[i][j] = False
                        return False
          #  board[i][j]="X"
            return True

        for i in range(ROWS) :
            for j in range(COLS) :
                if board[i][j]=="O" :
                    if dfs(i,j) :
                        board[i][j]="X"
        