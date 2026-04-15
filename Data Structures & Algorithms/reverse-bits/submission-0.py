class Solution:
    def reverseBits(self, n: int) -> int:
        s = f"{n:032b}"
        res=s[::-1]
        return int(res,2)