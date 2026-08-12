class Solution:
    def C(self, n, k) :
        res = 1

        for i in range(1,k+1):
            res = res * (n - i + 1) // i

        return res
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        for i in range(rowIndex+1):
            res.append(self.C(rowIndex,i))
        return res