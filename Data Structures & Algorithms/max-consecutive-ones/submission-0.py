class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,n=0,len(nums)
        i=0
        while i<n :
            while i<n and nums[i]!=1 :
                i+=1
            count=0
            while i<n and nums[i]==1 :
                count+=1
                i+=1
            m=max(m,count)
        return m