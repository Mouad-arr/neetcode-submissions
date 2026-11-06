class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        mp={}
        for pair in rectangles :
            ratio=pair[0]/pair[1]
            mp[ratio]=mp.get(ratio,0) + 1
        ans=0
        for p in mp.values():
            ans+= p*(p-1)//2
        return ans
