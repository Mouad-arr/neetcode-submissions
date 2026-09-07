class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0
        s.sort()
        g.sort()
        n,m=len(g),len(s)
        i,j=n-1,m-1
        count=0
        while i>=0 and j>=0:
            if g[i]<=s[j]:
                i-=1
                j-=1
                count+=1
            else:
                i-=1
        return count