class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        l,r=0,len(heights)-1
        while l<r :
            m=max((r-l)*min(heights[l],heights[r]),m)
            if heights[l] > heights[r] :
                r-=1
            elif heights[l] < heights[r] :
                l+=1
            else :
                while heights[l] == heights[r] and l<r :
                    if heights[l+1]>heights[r-1] :
                        l+=1
                    elif heights[l+1]<heights[r-1] :
                        r-=1
                    else :
                        r-=1
                        l+=1
        return m  
                     