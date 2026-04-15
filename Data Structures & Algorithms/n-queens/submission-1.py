class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        R=[]
        def dfs(i):
            if i>= n :
                R.append(["".join(board[k]) for k in range(n)])
                return
            for c in range(n):
                if 'Q' in [board[k][c] for k in range(i)] :
                    continue
                if 'Q' in [board[k][l] for k in range(i) for l in range(n) if k-l==i-c] :
                    continue 
                if 'Q' in [board[k][l] for k in range(i) for l in range(n) if k+l==i+c] :
                    continue
             
                board[i][c]='Q'
                dfs(i+1)
                board[i][c]='.'
            
        dfs(0)
        return R