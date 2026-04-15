class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        isVisited = [ [False for _ in range(len(board[0]))] for _ in range(len(board))]
        L,C=len(board),len(board[0])
        def dfs(ligne,col,i) :
            if i==len(word) :
                return True
            if ( min(ligne,col) <0 or ligne >= L or col>=C or board[ligne][col] != word[i] or isVisited[ligne][col] ):
                return False
            isVisited[ligne][col]=True
            res=(dfs(ligne-1,col,i+1) or dfs(ligne+1,col,i+1) or dfs(ligne,col-1,i+1) or dfs(ligne,col+1,i+1) )
            isVisited[ligne][col]=False
            return res
        for r in range(L):
            for c in range(C):
                if dfs(r,c,0)  :
                    return True
        return False