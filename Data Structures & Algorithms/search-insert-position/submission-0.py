class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<right :
            if nums[left]==target :
                return left
            elif nums[right]==target :
                return right
            elif nums[left]>target :
                return left
            elif nums[right]<target :
                return right +1 
            else :
                left+=1
                right-=1
        if nums[left]<target :
            return left+1
        else :
            return left