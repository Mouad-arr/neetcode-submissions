class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        left=0
        right=s-nums[0]
        i=0
        while left!=right and i+1<len(nums):
            left  += nums[i]
            right -= nums[i+1]
            i+=1
        if left!=right:
            return -1
        return i