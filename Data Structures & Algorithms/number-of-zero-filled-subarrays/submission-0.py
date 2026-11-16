class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        i=0
        while i<n :
            if nums[i]!=0:
                i+=1
            else :
                m=0
                while i<n and nums[i]==0:
                    m+=1
                    i+=1
                count+= (m*(m+1)//2)
        return count