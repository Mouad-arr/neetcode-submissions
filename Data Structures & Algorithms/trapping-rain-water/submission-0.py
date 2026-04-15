class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2 :
            return 0
        m=height[0]
        s=0
        for i in range(1,len(height)-1) :
            if height[i] > m :
                m=height[i]
            else :
                M=max(height[k] for k in range(i+1,len(height)))
                if height[i] < M :
                    s+=min(m,M) - height[i]
        return s