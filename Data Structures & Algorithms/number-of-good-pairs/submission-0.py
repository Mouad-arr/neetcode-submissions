class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        se=[]
        for e in set(nums):
            i=nums.count(e)
            if i>1:
                se.append(i)
        if len(se)==0:
            return 0
        m=max(se)
        s=0
        i=1
        cur=0
        while i<m:
            cur+=i
            if i+1 in se :
                s+= cur*(se.count(i+1))
            i+=1
        return s