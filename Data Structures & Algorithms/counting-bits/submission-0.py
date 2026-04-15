class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            x=bin(i)[2:]
            count =f"{x}"
            res.append(count.count("1"))
        return res
                