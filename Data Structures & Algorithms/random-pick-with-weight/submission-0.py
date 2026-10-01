class Solution:

    def __init__(self, w: List[int]):
        self.w=w
        self.index=0
        i,m=0,w[0]
        while i<len(w):
            if m<w[i]:
                self.index=i
                m=w[i]
            i+=1

    def pickIndex(self) -> int:
        return self.index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()