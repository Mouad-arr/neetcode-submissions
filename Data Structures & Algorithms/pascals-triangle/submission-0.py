class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        i=1
        while i<numRows :
            row=[1]
            j=0
            while j+1<i:
                row.append(res[i-1][j]+res[i-1][j+1])
                j+=1
            row.append(1)
            res.append(row)
            i+=1
        return res
            