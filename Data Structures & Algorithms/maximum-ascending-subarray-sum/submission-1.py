class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx=max(nums)
        i,n=0,len(nums)
        cur=0
        while i<n :
            if i+1 < n and nums[i]<nums[i+1] :
                cur = nums[i]+nums[i+1]
                i+=1
                while i+1 < n and nums[i]<nums[i+1] :
                    cur+=nums[i+1]
                    i+=1
                mx=max(mx,cur)
            else :
                i+=1
        return mx