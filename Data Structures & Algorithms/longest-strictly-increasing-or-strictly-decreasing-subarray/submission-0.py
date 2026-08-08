class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest=1
        n=len(nums)
        i=0
        cur=1
        while i<n :
            if i+1 < n and nums[i]<nums[i+1]:
                cur=2
                i+=1
                while i+1 < n and nums[i]<nums[i+1] :
                    i+=1
                    cur+=1
                longest=max(longest,cur)
            elif i+1<n and nums[i]>nums[i+1]:
                cur=2
                i+=1
                while i+1 < n and nums[i]>nums[i+1] :
                    i+=1
                    cur+=1
                longest=max(longest,cur)
            else :
                i+=1
        return longest        