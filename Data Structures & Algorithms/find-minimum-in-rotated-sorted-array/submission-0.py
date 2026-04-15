class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left <=right :
            if nums[left] <= nums[right] :
                return nums[left]
            else :
                m=(left+right)//2
                if nums[m] <nums[left] :
                    right=m
                else :
                    left=m+1
        return -1

        