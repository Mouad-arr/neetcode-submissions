class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        prefRow1,prefRow2 = grid[0].copy(),grid[1].copy()
        for i in range(1,m):
            prefRow1[i]+=prefRow1[i-1]
            prefRow2[i]+=prefRow2[i-1]
        res= float("inf")
        for i in range(m):
            top=prefRow1[-1]-prefRow1[i]
            if i>0:
                bottom=prefRow2[i-1]
            else:
                bottom = 0
            res = min(res,max(top,bottom))
        return res