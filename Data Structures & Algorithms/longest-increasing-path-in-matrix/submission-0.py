class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        d={}
        n=len(matrix)
        m=len(matrix[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j):
            if i < 0 or j < 0 or j >= m or i >= n:
                return 0
            if (i,j) in d :
                return d[(i,j)]
            res = 1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and matrix[i][j] < matrix[ni][nj]:
                    res = max(res, dfs(ni, nj) + 1)
            d[(i,j)]=res
            return res 
        M=0
        for i in range(n):
            for j in range(m):
                M=max(M,dfs(i,j))
        return M