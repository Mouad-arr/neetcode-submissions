class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0:
            return 0
        rows=[[poured]]
        for i in range(query_row):
            row=rows[i]
            length=len(row)
            new_row=[0]*(length+1)
            for j in range(length+1):
                if j>0 and j<length:
                    new_row[j]+=(row[j-1]-1)/2 + (row[j]-1)/2
                elif j==0:
                    new_row[j]=(row[j]-1)/2
                elif j==length:
                    new_row[j]=(row[j-1]-1)/2
            rows.append(new_row)
        if rows[query_row][query_glass] <0:
            return 0
        return min(1,rows[query_row][query_glass])