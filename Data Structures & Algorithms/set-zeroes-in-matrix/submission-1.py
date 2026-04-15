class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m=len(matrix),len(matrix[0])
        s=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    s.add((i,j))
        for (i,j) in s:
            for x in range(m):
                matrix[i][x]=0
            for x in range(n):
                matrix[x][j]=0