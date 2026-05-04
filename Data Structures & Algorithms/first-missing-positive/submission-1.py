class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        i=0
        while i<len(nums) and nums[i]<=0 :
            i+=1
        if i==len(nums):
            return 1
        else:
            k=1
            while  i < len(nums) and nums[i] == k:
                k+=1
                i+=1
            return k