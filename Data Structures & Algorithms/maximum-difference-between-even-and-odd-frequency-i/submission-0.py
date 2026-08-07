class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd=0
        minEven=float('INF')
        se=set(s)
        for c in se :
            count = s.count(c)
            if count % 2 == 0 :
                minEven=min(minEven,count)
            else :
                maxOdd=max(maxOdd,count)
        return maxOdd-minEven