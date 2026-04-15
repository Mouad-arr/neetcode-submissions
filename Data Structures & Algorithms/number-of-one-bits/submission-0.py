class Solution:
    def hammingWeight(self, n: int) -> int:
        s = f"{n:032b}"
        return s.count('1')