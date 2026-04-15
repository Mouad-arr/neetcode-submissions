class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        M=[]
        while left <= right :
            m=(right+left)//2
            L=sum([(x+m-1)//m for x in piles ])
            if L > h :
                left=m+1
            elif L <= h :
                right=m-1
                M.append(m)
        return min(M)
