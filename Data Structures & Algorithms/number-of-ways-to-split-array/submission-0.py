class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        count =0
        prefix=0
        i=0
        while i<n-1:
            s-=nums[i]
            prefix+=nums[i]
            if prefix>=s:
                count+=1
            i+=1
        return count

