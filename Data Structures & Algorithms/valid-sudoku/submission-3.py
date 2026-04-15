class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        L=[".","1","2","3","4","5","6","7","8","9"]
        isTrue = True
        for i in range(9) :
            Done=[]
            for l in board[i] :
                if (board[i].count(l) >1  or l not in L  ) and l!="." :
                    isTrue = False
                    break
            for j in range(9) :
                if board[j][i] not in L  or (board[j][i] in Done and board[j][i] != ".") :
                    isTrue = False
                    break
                Done.append(board[j][i])
        for i in range(0,9,3) :
            for j in range(0,9,3) :
                S=[]
                for k in range(3) :
                    for g in range(3) :
                        if board[i+k][j+g] in S and board[i+k][j+g] !="." :
                            isTrue=False
                            break
                        S.append(board[i+k][j+g])


        return isTrue